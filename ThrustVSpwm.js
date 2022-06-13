//To calculate thrust values at different PWM values

var PWMmin = 1200;
var PWMmax = 1500;
//var PWMstepsize = 20;
var minESC = 1000;

var params = {
    steps_qty: 30, 
    settlingTime_s: 5, // Settling time before measurement
    cooldownTime_s: 0, 
  //  cooldownThrottle_us: 1175,
  // cooldownMinThrottle: 1800, 
    max_slew_rate_us_per_s: 50
};
//var avgsamples = 30;

// new file
rcb.files.newLogFile({prefix : "MN7006_SUP15_SX_PWMvsThrust_25V"});

// Tare Load
rcb.sensors.tareLoadCells(ESCinit);

//Initialosation of ESC
function ESCinit()
{
    rcb.output.set("servo1", minESC);
    rcb.console.print("\n ESC initialised\n");
    rcb.wait(startSteps, 4);
}

function startSteps()
{
    takeSample(ramp);
}
function takeSample(callback){
    rcb.sensors.read(function (result){
        // Write the results and proceed to next step
        rcb.files.newLogEntry(result, callback); 
    }, 50);
}

function ramp()
{
    rcb.output.steps2("servo1", PWMmin, PWMmax, stepFct, finish, params);
}

function stepFct(nextStepFct)
{
    takeSample(nextStepFct);
}
function finish()
{
    // Calculate the ramp down time
    var rate = params.max_slew_rate_us_per_s;
    var time = 0;
    if(rate>0){
        time = (PWMmax-minESC) / rate;
    }
    rcb.output.ramp("servo1", PWMmax, minESC, time, endScript);
}
function endScript()
{
    rcb.endScript();
}


