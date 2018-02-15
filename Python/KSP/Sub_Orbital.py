import sys;
import krpc;
import time;
import math;
import datetime;

turn_start_altitude = 500;
turn_end_altitude = 35000;
target_altitude = 105000;

c_half_trun_alt = 10000;
c_full_turn_alt = 60000;

k = 45 / c_half_trun_alt;
k1 = 90 / c_full_turn_alt;

bHasSRBs = False;

def PrintVesselStatus(vessel):
	if(vessel is not None):
		tmpSas = vessel.control.sas;
		tmpSolid = vessel.resources.amount('SolidFuel');
		tmpLF = vessel.resources.amount('LiquidFuel');
		tmpO = vessel.resources.amount('Oxidizer');
		tmpElectric  = vessel.resources.amount("ElectricCharge");
		
		#SRBs available
		global bHasSRBs;
		if(tmpSolid > 0):
			bHasSRBs = True;
		
		print("[{0}]".format(datetime.datetime.now()));		
		print ("-------------------------Vessel---------------------------------");
		
		print("HasSRBs = {0}".format(bHasSRBs));
		
		tmpBuff  = "Status SolidFuel = {0}".format(tmpSolid);
		print( tmpBuff);
		
		tmpBuff  = "Status LiquidFuel = {0}".format(tmpLF);
		print( tmpBuff);
	
		tmpBuff  = "Status Oxidizer = {0}".format(tmpO);
		print( tmpBuff);
	
		tmpBuff  = "Status LiquidFuel = {0}".format(tmpElectric);
		print( tmpBuff);
	
		tmpBuff  = "Status S.A.S = {0}".format(tmpSas);
		print( tmpBuff);
		print ("-----------------------------------------------------------------");

def CalculateTurnAngle(altitude):	
	if(altitude > turn_start_altitude):
	
		if(altitude <= c_half_trun_alt):
			angle = math.floor(k * altitude);
		else:
			m = (45 - 90) / (c_half_trun_alt - c_full_turn_alt);
			
			tmpVal = m*(altitude - c_half_trun_alt) + 45;
			angle = math.floor(tmpVal);
			
		if(angle <= 90):
			return  angle;
		else:
			return 90;
	else:
		return  0;

def TestLegs(vessel, iTimeDelay):
	vessel.control.legs = True;
	print("Testing  landing legs...");
	
	time.sleep(iTimeDelay);
	vessel.control.legs = False;
	print("Testing  landing legs complete!");

def TestAirBreaks(vessel, iTimeDelay):
	vessel.control.brakes = True;
	print("Testing  air  brakes...");
	
	time.sleep(iTimeDelay);
	vessel.control.brakes = False;
	print("Testing  air brakes complete!");
	
def TestLandingGear(vessel, iTimeDelay):
	#test the gear
		vessel.control.gear = True;
		print("Testing  gear");
		time.sleep(iTimeDelay);
		vessel.control.gear = False;

def TestActionGroup(vessel, iTimeDelay):
	print("Test togle on  action group!");
	vessel.control.toggle_action_group(1);
	time.sleep(iTimeDelay+2);
	print("Test togle off  action group!");
	vessel.control.toggle_action_group(1);
	time.sleep(iTimeDelay);
		
def DeploySRBs():
	global bHasSRBs;
	#Check SRBs status
	if(bHasSRBs):
		#get solid fuel 
		tmpSolidF = vessel.resources.amount('SolidFuel');
		
		#check if stageing is needed
		if( tmpSolidF <= 5):
			vessel.control.activate_next_stage();
	
def DeployLandingLegs(vessel):
	vessel.control.toggle_action_group(1);

	
def VectorMagnitude(vector):
	return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] **2 );
#def PrintRpy(roll, )	


print("--------------Misson  control--------------\n");

#create connection	
conn = krpc.connect(name='Sub-orbital flight');

if (conn is not None):
	print("KSP Connection Succesfull");
else:
	sys.Exit(0);

#get active vessel
vessel = conn.space_center.active_vessel;

#trun off auto pilot
#vessel.auto_pilot.disengage();
vessel.auto_pilot.engage();

#try to activate S.A.S.
try:
	#vessel.auto_pilot.wait();
	vessel.control.sas = True;
	time.sleep(2);
	vessel.control.sas_mode  = conn.space_center.SASMode.prograde;
except:
	print("Unable to turn on SAS!");
	vessel.control.sas = False;
	time.sleep(5);

#do landing legs test
C_INT_TIME_DELAY = 5; #time delay in second

#TestLegs(vessel, C_INT_TIME_DELAY)	;
#TestLandingGear(vessel, C_INT_TIME_DELAY);
#TestAirBreaks(vessel, C_INT_TIME_DELAY);
#TestActionGroup(vessel, C_INT_TIME_DELAY);


PrintVesselStatus(vessel);

# Set up streams for telemetry
ut = conn.add_stream(getattr, conn.space_center, 'ut');
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude');
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude');
speedStr =  conn.add_stream(getattr, vessel.flight(), 'speed');
rollStr =  conn.add_stream(getattr, vessel.flight(), 'roll');


#stage 1 resources
stage_1_resources = vessel.resources_in_decouple_stage(stage=1, cumulative=False);
l_fuel = conn.add_stream(stage_1_resources.amount, 'LiquidFuel');
print("L f = %.2f" %l_fuel());
#stage 2 resources
stage_2_resources = vessel.resources_in_decouple_stage(stage=2, cumulative=False);
srb_fuel = conn.add_stream(stage_2_resources.amount, 'SolidFuel');



#get reference frame
ref_frame = conn.space_center.ReferenceFrame.create_hybrid(
    position=vessel.orbit.body.reference_frame,
    rotation=vessel.surface_reference_frame)

	
#Open bug
#print(vessel.auto_pilot.sas_mode);
#vessel.control.sas = True;
#time.sleep(10);
#vessel.control.sas_mode  = conn.space_center.SASMode.prograde;
#print(vessel.auto_pilot.sas_mode);


#set heding
vessel.auto_pilot.target_pitch_and_heading(90, 90);
vessel.control.throttle = 1;

#10 seconds countdown
counter = 5;
while (counter >= 0):
	time.sleep(1);
	print( "T - {0}".format(counter) );
	counter-=1;

#lanch

#turn engines off
vessel.control.activate_next_stage();

time.sleep(5);

print('Launch!');
vessel.control.activate_next_stage();

prevVel = 0;
currVel  = 0;

currAlt = 0;
currAppo = 0;
currAcc= 0;

c_target_vel = 230;
turn_angle = 0;
currThr = 0.7;

curFl =  vessel.flight();
bNextSt= True;
#execute  stage and turn to apoapsis
while  (  target_altitude - apoapsis() >= 0.05 ):

	#get velocity vector
	velocity = vessel.flight(ref_frame).velocity;
	
	#telemetry data
	currVel = velocity[0];
	currAlt = altitude();	
	currAppo = apoapsis();
	currAcc = vessel.thrust / vessel.mass;
	currSpeed =  vessel.flight(ref_frame).speed;
	
	#delta velocity
	dVel = (currVel - prevVel);	
	
	if(currAlt < 10000):
		if(currVel - c_target_vel > 10 and  currAcc > 15):
			vessel.control.throttle = currThr ;#(c_target_vel / currVel);
			currThr -= 0.05;
			print("Throtile down!. Throtile =  %.2f" % vessel.control.throttle);
		elif(currVel - c_target_vel > 10 and  currAcc < 14):
			currThr  += 0.05;
			vessel.control.throttle = currThr ;#(c_target_vel / currVel);		
			print("Throtile up!. Throtile =  %.2f" % vessel.control.throttle);	
	#abouve 10k alt and 60m/s2 acc  throttle down to 75% !!
	elif ( (currAlt > 10000) and (currAlt < 30000) and (currSpeed > 800)):
		if(vessel.control.throttle > 0.5):
			vessel.control.throttle -= 0.05;
			print("Throtile down!. Throtile =  %.2f" % vessel.control.throttle);
	elif ( (currAlt > 10000) and (currAlt < 30000) and (currSpeed  < 850) and (vessel.control.throttle < 1) ):
		vessel.control.throttle +=  0.05;
		print("Throtile up!. Throtile =  %.2f" % vessel.control.throttle);
	elif( currAcc > 60 and vessel.control.throttle > 0  ):
		vessel.control.throttle -= 0.05;
		print("Throtile down!. Throtile =  %.2f" % vessel.control.throttle);
	elif( (currAlt < 30000) and  (currAcc <= 60) and (vessel.control.throttle < 1) ):
		vessel.control.throttle +=  0.05;
		print("Throtile up!. Throtile =  %.2f" % vessel.control.throttle);
	#TOelif(currVel)
	#else:
	#	vessel.control.throttle = 0;
	#	vessel.auto_pilot.disengage();
	#	print("Throtile to 0. Autopilot off");
	
	 # Gravity turn
	turn_angle = CalculateTurnAngle(currAlt);	
	vessel.auto_pilot.target_pitch_and_heading(90-turn_angle, 90);
	#print("turn_angle = %.2f" %(turn_angle));
	
	#deploy if any SRBs
	DeploySRBs();
	
	#stage if needed
	if(vessel.resources.amount('LiquidFuel') < 10 and bNextSt):
		bNextSt = False;
		vessel.control.activate_next_stage();
		time.sleep(1);
		vessel.control.activate_next_stage();
	
	print("Velocity = %.2f, Speed = %.2f Altitute = %.2f, DeltaVel = %.2f, Accel= %.2f Apoapsis = %.2f Turn Angle = %.2f" % (currVel, currSpeed, currAlt, dVel, currAcc, currAppo, turn_angle));	
	#print("Roll = {0}".format( rollStr() ) );
	prevVel =currVel;
	
	#wait for one second
	time.sleep(1);

vessel.control.throttle = 0;
vessel.auto_pilot.disengage();	

print("Sub-orbital burn complete. Current orbit apoapsis = {0}".format( vessel.orbit.apoapsis_altitude) );
time.sleep(2);

C_SPACE_BORDER = 70000;	
C_VESSEL_HEADING = 90;
ap= vessel.auto_pilot;

print("Performing flight procedures after initial burn!");
#try to hold heding
while ( ( apoapsis() - altitude() ) > 2000) :
	#set throttle to 0
	
	roll =  curFl.roll;
	pitch = curFl.pitch;
	heading = curFl.heading;
	print("R = %.2f, P= %.2f, H = %.2f" %(roll, pitch, heading) );
	
	if(vessel.control.throttle != 0):
		vessel.control.throttle = 0;

	#perform heading correction above 70k altitude
	if(altitude() > C_SPACE_BORDER):
		if( abs(heading - C_VESSEL_HEADING) > 2.0  or ( abs(curFl.pitch) - 2.0 >  1 ) ) :
		
			#turn on rcs and auto_pilot
			vessel.control.rcs = True;			
			ap.engage();
			
			print("R = %.2f, P = %.2f, H = %.2f" %(curFl.roll, curFl.pitch, curFl.heading) );
			
			print("Aligning the vessel to (0, 90, 0 )");		
			print("RCS: {0}".format(vessel.control.rcs));
			print("Autopilot ON");
			
			print("Perform manuvering turn...");
			ap.target_roll = 0;
			ap.wait();
			ap.target_pitch_and_heading(0, C_VESSEL_HEADING);
			ap.wait();
			time.sleep(1);
			print("Manuvering turn complete...");
			
			#disable rcs
			#if(vessel.control.rcs):
			#	vessel.control.rcs = False;
	
	time.sleep(1);
	

DeployLandingLegs(vessel);


#set prograde
ap.engage();
vessel.control.rcs = True;

print("Set heading to west (270 deg)");
ap.target_roll = 0;
ap.wait();
ap.target_heading = 270;
ap.wait();
vessel.control.rcs = False;

#test  the landing legs		