const signalR = require("@microsoft/signalr");
const connection = new signalR.HubConnectionBuilder()
    .withUrl("https://power-hack.azurewebsites.net/liveMeasurement")
    .configureLogging(signalR.LogLevel.Information)
    .build();


function aggregateDataPoint(dataPoint) {
    console.log(dataPoint);
}

async function start() {
    try {
        await connection.start();
        console.log("SignalR Connected.");

        // Replace <MeteringpointId>
        connection.stream("Subscribe", "707057500100175148").subscribe({
            next: aggregateDataPoint,
            complete: () => console.log("stream completed"),
            error: (err) => console.log(err)
        })
    } catch (err) {
        console.log(err);
        setTimeout(start, 5000);
    }
};

start();