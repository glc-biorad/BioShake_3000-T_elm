# BioShake_3000-T_elm
BioShake 3000-T elm class for control of heater/shaker.

# Current State:
Currently tests a majority of the BioShake 3000-T elm's functionality, including shaking at a specified rpm, setting/changing/holding the temperature in degrees C, etc.

# Commands Overview:
  - # Initialization:
    - info: returns a list of general information
    - getVersion: returns the current firmware version number
    - getDescription: returns the current model information
    - resetDevice: restarts the controller (this takes about 30 sec)
    - getErrorList: returns a semicolon-separated list with errors and warnings that occurred during processing
    - enableCLED: permanent activation of the LED indication lights (the instrument will reset after this command)
    - disableCLED: permanent deactivation of the LED indication light (the instrument will reset after this command)
  - # ECO mode:
    - setEcoMode: switches the shaker into economical mode, reducing electricity consumption by deactivating the solenoid for the homing position and deactivation of the ELM function
    - leaveEcoMode: leaves the economical mode and switches into the normal operating state
  - # Shaking & Homing zero position control:
    - shakeOn: starts the shaking with the current mixing speed
    - shakeOnWithRuntime: starts the shaking with the current mixing speed for a defined time in seconds
    - getShakeRemainingTime: returns the remaining time in seconds of a single program
    - shakeOff: stops the shaking, proceeds to the homing position and locks in place
    - shakeOffWithDeenergizeSolenoid: stops the shaking, proceeds to the homing position, locks in place for 1 sec, then unlock zero position
    - shakeGoHome: shaker moves to the homing zero position and locks in place
    - shakeOffNonZeroPos: fast and safe stopping of all movements
    - shakeEmergencyOff:  fast and safe stopping of all movements
    - getShakeState: returns the state of shaking
      - value 0 Shaking is active
      - value 1 Shaker has a stop command detect
      - value 2 Shaker in the braking mode
      - value 3 Arrived in the home position
      - value 4 Manual mode for external control
      - value 5 Acceleration
      - value 6 Deceleration
      - value 7 Deceleration with stopping
      - value 90 ECO mode
      - value 99 Boot process running
    - getShakeStateAsString: returns the state of shaking as a string
      - value RAMP+ Acceleration
      - value RAMP- Deceleration
      - value RUN Running
      - value STOP Arrived in home position
      - value ESTOP Emergency stop
    - getShakeZPV
