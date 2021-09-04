const signalR = require("@microsoft/signalr");
const { MongoClient } = require("mongodb");
const connection = new signalR.HubConnectionBuilder()
  .withUrl("https://power-hack.azurewebsites.net/liveMeasurement")
  .configureLogging(signalR.LogLevel.Information)
  .build();

const uri =
  "mongodb+srv://db_user:very_simple_password@cluster0.eu0ag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

let buffer = [];

function dumpToDatabase(dataPoints) {
  const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
  client.connect((err) => {
    const collection = client.db("han-data").collection("datapoints");
    collection.insertMany(dataPoints, (err, res) => {
      client.close();
    });
    // perform actions on the collection object
  });
}

function aggregateDataPoint(dataPoint) {
  buffer.push(dataPoint);
  if (buffer.length >= 10) {
    console.log("Dumping to database");
    dumpToDatabase(buffer);
    buffer = [];
  }
}

async function start() {
  try {
    await connection.start();
    console.log("SignalR Connected.");

    // Replace <MeteringpointId>
    connection.stream("Subscribe", "707057500100175148").subscribe({
      next: aggregateDataPoint,
      complete: () => console.log("stream completed"),
      error: (err) => console.log(err),
    });
  } catch (err) {
    console.log(err);
    setTimeout(start, 5000);
  }
}

start();
