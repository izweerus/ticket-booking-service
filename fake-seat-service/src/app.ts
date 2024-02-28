////////////////////////////////////
// FAKE SEAT RESERVATION SERVICE
////////////////////////////////////
import { ZBClient } from "zeebe-node";
require("dotenv").config();

const zeebeClient = new ZBClient();
const worker = zeebeClient.createWorker('reserve-seats', reserveSeatsHandler)

function reserveSeatsHandler(job, _, worker) {  
  console.log("\n\n Reserve seats now...");
  console.log(job);

  // Do the real reservation
  // TODO: Fake some results! Fake an error (when exactly?)
  if ("seats" !== job.variables.simulateBookingFailure) {
    console.log("Successul :-)");
    return job.complete({
        reservationId: "1234",
      });
  } else {
    console.log("ERROR: Seats could not be reserved!");
    return job.error("ErrorSeatsNotAvailable");
  }
}