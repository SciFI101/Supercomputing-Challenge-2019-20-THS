'''All determination of symptoms is based on patient's answers
and has no professional determination. The program is intended to
provide a basic diagnostic and give the doctor a thesis for
the patient's affliction.'''
'''Henry, if you could integrate the shared symptoms system for our machine learning section by
tomorrow I would greatly appreciate it.'''
from SCProjDictionaries import LowerRespiratoryTractInfection, TheFlu, Conjunctivitis, Tuberculosis, EarInfection, Myocaditus, Cardiomegaly
def getPatientInputInitial():
	global AilmentQuery
	AilmentQuery = input('What do you believe you are suffering from? ')
	#Determines the questionaire based on the input provided. Very few ailments are listed here.
	if AilmentQuery.lower() == 'lrti': #Stands for Lower Respiratory Tract Infection
		getPatientInputLRTI()
	elif AilmentQuery.lower() == 'the flu':
		getPatientInputTheFlu()
	elif AilmentQuery.lower() == 'conjunctivitis': #Pink Eye
		getPatientInputConjunctivitis()
	elif AilmentQuery.lower() == 'tuberculosis':
		getPatientInputTuberculosis()
	elif AilmentQuery.lower() == 'ear infection':
		getPatientInputEarInfection()
	elif AilmentQuery.lower() == 'myocaditus':
		getPatientInputMyocaditus()
	elif AilmentQuery.lower() == 'cardiomegaly':
		getPatientInputCardiomegaly()
	elif AilmentQuery.lower() == 'idk' or AilmentQuery.lower() == "i don't know":
		getPatientInputIDK() #Define this shit now!
	else:
		print('Input not recognized please retype below.')
		getPatientInputInitial()

def getPatientInputLRTI():#Queries for LRTI
	global ShortnessOfBreath
	global Weakness
	global Fever
	global Coughing
	global Fatigue
	global AddSym
	ShortnessOfBreath = input('Do you have shortness of breath?  Y/N: ')
	Weakness = input('Do you feel weak?  Y/N: ')
	Fever = input('Do you have a fever?  Y/N: ')
	Coughing = input('Are you coughing?  Y/N: ')
	Fatigue = input('Are you fatigued?  Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Shortness of Breath = ' + ShortnessOfBreath)
	print ('Weakness = ' + Weakness)
	print ('Fever = ' + Fever)
	print ('Coughing = ' + Coughing)
	print ('Fatigue = ' + Fatigue)

def getPatientInputTheFlu():#Queries for The Flu
	global Fever
	global Coughing
	global SoreThroat
	global RunnyStuffyNose
	global MuscleBodyAches
	global Headaches
	global Fatigue
	global VomitingAndDiahrrea
	global AddSym
	Fever = input('Do you have a fever?  Y/N: ')
	Coughing = input('Are you coughing?  Y/N: ')
	SoreThroat = input('Do you have a sore throat?  Y/N: ')
	RunnyStuffyNose = input('Do you have a runny/stuffy nose?  Y/N: ')
	MuscleBodyAches = input('Do you have muscle/body aches?  Y/N: ')
	Headaches = input('Do you get headaches? Y/N: ')
	Fatigue = input('Are you fatigued? Y/N: ')
	VomitingAndDiahrrea = input('Do you vomit or have diarrhea? Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Fever = ' + Fever)
	print ('Coughing = ' + Coughing)
	print ('Sore throat = ' + SoreThroat)
	print ('Runny/stuffy nose = ' + RunnyStuffyNose)
	print ('Muscle/body aches = ' + MuscleBodyAches)
	print ('Headaches = ' + Headaches)
	print ('Fatigue = ' + Fatigue)
	print ('Vomit/diarrhea = ' + VomitingAndDiahrrea)

def getPatientInputConjunctivitis():#Queries for Conjunctivitis/Pink Eye
	global RedEyes
	global IcthyEyes
	global GrittyEyes
	global CrustyEyes
	global Tearing
	global AddSym
	RedEyes = input('Are either of your eyes red?  Y/N: ')
	IcthyEyes = input('Are either of your eyes itchy?  Y/N: ')
	GrittyEyes = input('Do your eyes feel gritty?  Y/N: ')
	CrustyEyes = input('Are either of your eyes producing a liquid that becomes crusty?  Y/N: ')
	Tearing = input('Are either of your eyes tearing?  Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Redness in one or both eyes = ' + RedEyes)
	print ('Itchiness in one or both eyes = ' + IcthyEyes)
	print ('Gritty feeling in one or both eyes = ' + GrittyEyes)
	print ('One or both eyes discharging a liquid that becomes a crust = ' + CrustyEyes)
	print ('Tearing = ' + Tearing)

def getPatientInputTuberculosis():#Queries for Tuberculosis
	global Cough3Weeks
	global CoughBlood
	global ChestPainResp
	global WeightLoss
	global Fatigue
	global Fever
	global NightSweats
	global Chills
	global AppetiteLoss
	global AddSym
	Cough3Weeks = input('Have you been coughing for 3 or more weeks?  Y/N: ')
	CoughBlood = input('Are you coughing up blood?  Y/N: ')
	ChestPainResp = input('Do you have chest pain/pain while breathing/coughing?  Y/N: ')
	WeightLoss = input('Are you losing wirght unintentionally?  Y/N: ')
	Fatigue = input('Are you fatigued?  Y/N: ')
	Fever = input('Do you have a fever? Y/N: ')
	NightSweats = input('Do you sweat at night? Y/N: ')
	Chills = input('Do you get chills? Y/N: ')
	AppetiteLoss = input('Do you lose your appetite? Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Coughing for 3 or more weeks = ' + Cough3Weeks)
	print ('Coughing up blood = ' + CoughBlood)
	print ('Chest pain/pain while breathing/coughing = ' + ChestPainResp)
	print ('Unintentional weight loss = ' + WeightLoss)
	print ('Fatigue = ' + Fatigue)
	print ('Fever = ' + Fever)
	print ('Night Sweats = ' + NightSweats)
	print ('Chills = ' + Chills)
	print ('Loss of Appetite' + AppetiteLoss)

def getPatientInputEarInfection():#Queries for an Ear Infection
	global Earache
	global EarFull
	global EarPain
	global MuffledHear
	global EarDrain
	global AddSym
	Earache = input('Do either of your ears ache?  Y/N: ')
	EarFull = input('Do either of your ears feel full?  Y/N: ')
	EarPain = input('Do either of your ears give a sharp pain?  Y/N: ')
	MuffledHear = input('Is your hearing muffled in either ear?  Y/N: ')
	EarDrain = input('Does either ear drain a liquid?  Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Earache = ' + Earache)
	print ('Feeling of fullness in the ear = ' + EarFull)
	print ('Sharp pain in the ear = ' + EarPain)
	print ('Muffled hearing = ' + MuffledHear)
	print ('Ear drainage = ' + EarDrain)

def getPatientInputMyocaditus():#Queries for Myocaditus
	global ChestPain
	global HeartArrythmia
	global ShortnessOfBreath
	global LowAppendageSwell
	global Fatigue
	global ViralInfection
	global AddSym
	ChestPain = input('Do you have chest pain?  Y/N: ')
	HeartArrythmia = input('Do you have an abnormal heartbeat?  Y/N: ')
	ShortnessOfBreath = input('Do you have shortness of breath?  Y/N: ')
	LowAppendageSwell = input('Are your legs, feet, and toes swelling?  Y/N: ')
	Fatigue = input('Are you fatigued?  Y/N: ')
	ViralInfection = input('Do you have a viral infection? Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Chest pain = ' + ChestPain)
	print ('Heart Arrythmia = ' + HeartArrythmia)
	print ('Shortness of breath = ' + ShortnessOfBreath)
	print ('Swelling in the the lower appendages = ' + LowAppendageSwell)
	print ('Fatigue = ' + Fatigue)
	print ('Viral infection (headache, body aches, fever, sore throat, diarrhea)' + ViralInfection)

def getPatientInputCardiomegaly():#Queries for Cardiomegaly
	global AbdomenalSwell
	global HeartArrythmia
	global ChestPain
	global Coughing
	global Dizziness
	global Fatigue
	global ShortnessOfBreath
	global LowAppendageSwell
	global AddSym
	AbdomenalSwell = input('Is your abdomen bloating?  Y/N: ')
	HeartArrythmia = input('Do you have an abnormal heartbeat?  Y/N: ')
	ChestPain = input('Do you have chest pain?  Y/N: ')
	Coughing = input('Do you cough, especially lying down?  Y/N: ')
	Dizziness = input('Do you regularly become dizzy?  Y/N: ')
	Fatigue = input('Are you fatigued? Y/N: ')
	ShortnessOfBreath = input('Do you have shortness of breath? Y/N: ')
	LowAppendageSwell = input('Are your legs, feet, and toes swelling? Y/N: ')
	AddSym = input('Is there any other information or symptoms you would like to provide? ')
	print ('Abdominal bloating = ' + AbdomenalSwell)
	print ('Heart Arrythmia = ' + HeartArrythmia)
	print ('Chest pain = ' + ChestPain)
	print ('Coughing (especially when lying down) = ' + Coughing)
	print ('Dizziness = ' + Dizziness)
	print ('Fatigue = ' + Fatigue)
	print ('Shortness of breath = ' + ShortnessOfBreath)
	print ('Swelling in the the lower appendages = ' + LowAppendageSwell)

def getPatientInputIDK():
	global ShortnessOfBreath
	global Weakness
	global Fever
	global Coughing
	global Fatigue
	global SoreThroat
	global RunnyStuffyNose
	global MuscleBodyAches
	global Headaches
	global VomitingAndDiahrrea
	global RedEyes
	global IcthyEyes
	global GrittyEyes
	global CrustyEyes
	global Tearing
	global Cough3Weeks
	global CoughBlood
	global ChestPainResp
	global WeightLoss
	global NightSweats
	global Chills
	global AppetiteLoss
	global Earache
	global EarFull
	global EarPain
	global MuffledHear
	global EarDrain
	global ChestPain
	global HeartArrythmia
	global ShortnessOfBreath
	global LowAppendageSwell
	global ViralInfection
	global AbdomenalSwell
	global HeartArrythmia
	global ChestPain
	global Dizziness
	global LowAppendageSwell
	global AddSym
	print('Since you do not know what is affecting you, you must describe the symptoms you have to determine what is most likely affecting you.')
	ShortnessOfBreath = input('Do you have shortness of breath?')
	if ShortnessOfBreath.lower() == 'y' or ShortnessOfBreath.lower() == 'yes':
		Weakness = input('Do you feel weak?')
		if Weakness.lower() == 'y' or Weakness.lower() == 'yes':
			Fever = input('Do you have a fever?')
			Coughing = input('Are you coughing?')
			Fatigue = input('Are you fatigued?')
			LRTIConversion()
			LRTIDiagnose()
			exit()
	SoreThroat = input('Is your throat sore?')
	if SoreThroat.lower() == 'y' or SoreThroat.lower() == 'yes':
		RunnyStuffyNose = input('Is your nose runny or stuffy?')
		if RunnyStuffyNose == 'y' or RunnyStuffyNose == 'yes':
			MuscleBodyAches = input('Do your muscles or whole body ache?')
			Headaches = input('Do you get headaches consistently?')
			VomitingAndDiahrrea =('Do you vomit and/or have have diarrhea?')
			Fever = input('Do you have a fever?')
			Coughing = input('Do you cough frequently?')
			Fatigue = input('Are you fatigued?')
			theFluConversion()
			theFluDiagnose()
			exit()
	RedEyes = input('Are your eyes red?')
	if RedEyes.lower() == 'y' or RedEyes.lower() == 'yes':
		IcthyEyes = input('Are your eyes itchy?')
		GrittyEyes = input('Are your eyes gritty?')
		CrustyEyes = input ('Are your eyes crusty?')
		Tearing = input ('Are your eyes tearing up?')
		conjunctivitisConversion()
		conjunctivitisDiagnose()
		exit()
	Cough3Weeks = input('Have you been coughing consistently for about 3 weeks?')
	if Cough3Weeks.lower() == 'y' or Cough3Weeks.lower() == 'yes':
		CoughBlood = input('Have you been coughing up blood?')
		if CoughBlood.lower() == 'y' or CoughBlood.lower() == 'yes':
			ChestPainResp = input('Does your upper chest hurt?')
			WeightLoss = input('Have you been losing weight?')
			Fatigue = input ('Are you fatigued?')
			Fever = input('Do you have a fever?')
			NightSweats = input('Do you sweat at night?')
			Chills = input('Do you get chills?')
			AppetiteLoss = input('Have you had a loss of appetite?')
			tuberculosisConversion()
			tuberculosisDiagnose()
			exit()
	Earache = input('Do your ears ache?')
	if Earache.lower() == 'y' or Earache.lower() == 'yes':
		EarFull = input('Do your ears feel full?')
		EarPain = input('Do your eyes give a sharp pain?')
		MuffledHear = input('Is your hearing muffled?')
		EarDrain = input('Do your ears drain a liquid?')
		earInfectionConversion()
		earInfectionDiagnose()
		exit()
	LowAppendageSwell = input('Are your lower appendages swelling?')
	if LowAppendageSwell.lower() == 'y' or LowAppendageSwell.lower() == 'yes':
		ViralInfection = input('Do you have any type of viral infection?')
		if ViralInfection.lower() == 'y' or ViralInfection.lower() == 'yes':
			ChestPain = input('Does your shect hurt?')
			HeartArrythmia = input('Do you have an abnormal heartbeat?')
			ShortnessOfBreath = input('Do you have shortness of breath?')
			Fatigue = input('Are you fatigued?')
			myocaditusConversion()
			myocaditusDiagnose()
			exit()
	if LowAppendageSwell == 'y' or LowAppendageSwell == 'yes':
		Dizziness = input('Are you dizzy?')
		if Dizziness.lower() == 'y' or Dizziness.lower() == 'yes':
			AbdomenalSwell = input('Is your abdomen swelling?')
			Fatigue = input('Are you fatigued?')
			HeartArrythmia = input('Do you have an abnormal heartbeat?')
			ChestPain = input('Does your chest hurt?')
			Coughing = input('Are you coughing consistently?')
			ShortnessOfBreath = input('Do you have shortness of breath?')
			cardiomegalyConversion()
			cardiomegalyDiagnose()
			exit()
	else:
		print('Unable to create sepcified profile set for the patient. Patient, please see a proper medical professional for your preliminary screening.')
		exit()

def convertToInteger():#This function doesn't actually convert the strings, it decides which program to use based on the original ailment choice
	global AilmentQuery
	if AilmentQuery.lower() == 'lrti':
		LRTIConversion()
	elif AilmentQuery.lower() == 'the flu':
		theFluConversion()
	elif AilmentQuery.lower() == 'conjunctivitis':
		conjunctivitisConversion()
	elif AilmentQuery.lower() == 'tuberculosis':
		tuberculosisConversion()
	elif AilmentQuery.lower() == 'ear infection':
		earInfectionConversion()
	elif AilmentQuery.lower() == 'myocaditus':
		myocaditusConversion()
	elif AilmentQuery.lower() == 'cardiomegaly':
		cardiomegalyConversion()
	elif AilmentQuery.lower() == 'idk' or AilmentQuery.lower() == "i don't know":
		IDKConversion()

def LRTIConversion(): #LRTI's conversion to integers
	global ShortnessOfBreathInt
	global WeaknessInt
	global FeverInt
	global CoughingInt
	global FatigueInt

	global ShortnessOfBreath
	global Weakness
	global Fever
	global Coughing
	global Fatigue

	if ShortnessOfBreath.lower() == 'y':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'yes':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'n':
		ShortnessOfBreathInt = 0
	elif ShortnessOfBreath.lower() == 'no':
		ShortnessOfBreathInt = 0
	else:
		ShortnessOfBreath = input('Input not recognized for shortness of breath, please retype Y/N. ')
		LRTIConversion()
	if Weakness.lower() == 'y':
		WeaknessInt = 1
	elif Weakness.lower() == 'yes':
		WeaknessInt = 1
	elif Weakness.lower() == 'n':
		WeaknessInt = 0
	elif Weakness.lower() == 'no':
		WeaknessInt = 0
	else:
		Weakness = input('Input not recognized for weakness, please retype Y/N. ')
		LRTIConversion()
	if Fever.lower() == 'y':
		FeverInt = 1
	elif Fever.lower() == 'yes':
		FeverInt = 1
	elif Fever.lower() == 'n':
		FeverInt = 0
	elif Fever.lower() == 'no':
		FeverInt = 0
	else:
		Fever = input('Input not recognized for fever, please retype. Y/N. ')
		LRTIConversion()
	if Coughing.lower() == 'y':
		CoughingInt = 1
	elif Coughing.lower() == 'yes':
		CoughingInt = 1
	elif Coughing.lower() == 'n':
		CoughingInt = 0
	elif Coughing.lower() == 'no':
		CoughingInt = 0
	else:
		Coughing = input('Input not recognized for coughing, please retype. Y/N. ')
		LRTIConversion()
	if Fatigue.lower() == 'y':
		FatigueInt = 1
	elif Fatigue.lower() == 'yes':
		FatigueInt = 1
	elif Fatigue.lower() == 'n':
		FatigueInt = 0
	elif Fatigue.lower() == 'no':
		FatigueInt = 0
	else:
		Fatigue = input('Input not recognized for fatigue, please retype. Y/N. ')
		LRTIConversion()

def theFluConversion(): #The Flu's conversion to integers
	global FeverInt
	global CoughingInt
	global SoreThroatInt
	global RunnyStuffyNoseInt
	global MuscleBodyAchesInt
	global HeadachesInt
	global FatigueInt
	global VomitingAndDiahrreaInt

	global Fever
	global Coughing
	global SoreThroat
	global RunnyStuffyNose
	global MuscleBodyAches
	global Headaches
	global Fatigue
	global VomitingAndDiahrrea

	if Fever.lower() == 'y':
		FeverInt = 1
	elif Fever.lower() == 'yes':
		FeverInt = 1
	elif Fever.lower() == 'n':
		FeverInt = 0
	elif Fever.lower() == 'no':
		FeverInt = 0
	else:
		Fever = input('Input not recognized for fever, please retype Y/N. ')
		theFluConversion()
	if Coughing.lower() == 'y':
		CoughingInt = 1
	elif Coughing.lower() == 'yes':
		CoughingInt = 1
	elif Coughing.lower() == 'n':
		CoughingInt = 0
	elif Coughing.lower() == 'no':
		CoughingInt = 0
	else:
		Coughing = input('Input not recognize for coughing, please retype Y/N. ')
		theFluConversion()
	if SoreThroat.lower() == 'y':
		SoreThroatInt = 1
	elif SoreThroat.lower() == 'yes':
		SoreThroatInt = 1
	elif SoreThroat.lower() == 'n':
		SoreThroatInt = 0
	elif SoreThroat.lower() == 'no':
		SoreThroatInt = 0
	else:
		SoreThroat = input('Input not recognized for sore throat, please retype. Y/N. ')
		theFluConversion()
	if RunnyStuffyNose.lower() == 'y':
		RunnyStuffyNoseInt = 1
	elif RunnyStuffyNose.lower() == 'yes':
		RunnyStuffyNoseInt = 1
	elif RunnyStuffyNose.lower() == 'n':
		RunnyStuffyNoseInt = 0
	elif RunnyStuffyNose.lower() == 'no':
		RunnyStuffyNoseInt = 0
	else:
		RunnyStuffyNose = input('Input not recognized for runny/stuffy nose, please retype. Y/N. ')
		theFluConversion()
	if MuscleBodyAches.lower() == 'y':
		MuscleBodyAchesInt = 1
	elif MuscleBodyAches.lower() == 'yes':
		MuscleBodyAchesInt = 1
	elif MuscleBodyAches.lower() == 'n':
		MuscleBodyAchesInt = 0
	elif MuscleBodyAches.lower() == 'no':
		MuscleBodyAchesInt = 0
	else:
		MuscleBodyAches = input('Input not recognized for muscle/body aches, please retype. Y/N. ')
		theFluConversion()
	if Headaches.lower() == 'y':
		HeadachesInt = 1
	elif Headaches.lower() == 'yes':
		HeadachesInt = 1
	elif Headaches.lower() == 'n':
		HeadachesInt = 0
	elif Headaches.lower() == 'no':
		HeadachesInt = 0
	else:
		Headaches = input('Input not recognized for headaches, please retype. Y/N. ')
		theFluConversion()
	if Fatigue.lower() == 'y':
		FatigueInt = 1
	elif Fatigue.lower() == 'yes':
		FatigueInt = 1
	elif Fatigue.lower() == 'n':
		FatigueInt = 0
	elif Fatigue.lower() == 'no':
		FatigueInt = 0
	else:
		Fatigue = input('Input not recognized for fatigue, please retype. Y/N. ')
		theFluConversion()
	if VomitingAndDiahrrea.lower() == 'y':
		VomitingAndDiahrreaInt = 1
	elif VomitingAndDiahrrea.lower() == 'yes':
		VomitingAndDiahrreaInt = 1
	elif VomitingAndDiahrrea.lower() == 'n':
		VomitingAndDiahrreaInt = 0
	elif VomitingAndDiahrrea.lower() == 'no':
		VomitingAndDiahrreaInt = 0
	else:
		VomitingAndDiahrrea = input('Input not recognized for vomiting and diahrrea, please retype. Y/N. ')
		theFluConversion()

def conjunctivitisConversion(): #Conjunctivitis/Pink Eye's conversion to integers
	global RedEyesInt
	global IcthyEyesInt
	global GrittyEyesInt
	global CrustyEyesInt
	global TearingInt

	global RedEyes
	global IcthyEyes
	global GrittyEyes
	global CrustyEyes
	global Tearing

	if RedEyes.lower() == 'y':
		RedEyesInt = 1
	elif RedEyes.lower() == 'yes':
		RedEyesInt = 1
	elif RedEyes.lower() == 'n':
		RedEyesInt = 0
	elif RedEyes.lower() == 'no':
		RedEyesInt = 0
	else:
		RedEyes = input('Input not recognized for redness in either eye, please retype Y/N. ')
		conjunctivitisConversion()
	if IcthyEyes.lower() == 'y':
		IcthyEyesInt = 1
	elif IcthyEyes.lower() == 'yes':
		IcthyEyesInt = 1
	elif IcthyEyes.lower() == 'n':
		IcthyEyesInt = 0
	elif IcthyEyes.lower() == 'no':
		IcthyEyesInt = 0
	else:
		IcthyEyes = input('Input not recognized for itchiness in either eye, please retype Y/N. ')
		conjunctivitisConversion()
	if GrittyEyes.lower() == 'y':
		GrittyEyesInt = 1
	elif GrittyEyes.lower() == 'yes':
		GrittyEyesInt = 1
	elif GrittyEyes.lower() == 'n':
		GrittyEyesInt = 0
	elif GrittyEyes.lower() == 'no':
		GrittyEyesInt = 0
	else:
		GrittyEyes = input('Input not recognized for gritty feeling in either eye, please retype. Y/N. ')
		conjunctivitisConversion()
	if CrustyEyes.lower() == 'y':
		CrustyEyesInt = 1
	elif CrustyEyes.lower() == 'yes':
		CrustyEyesInt = 1
	elif CrustyEyes.lower() == 'n':
		CrustyEyesInt = 0
	elif CrustyEyes.lower() == 'no':
		CrustyEyesInt = 0
	else:
		CrustyEyes = input('Input not recognized for either eye producing a liquid that becomes a crust, please retype. Y/N. ')
		conjunctivitisConversion()
	if Tearing.lower() == 'y':
		TearingInt = 1
	elif Tearing.lower() == 'yes':
		TearingInt = 1
	elif Tearing.lower() == 'n':
		TearingInt = 0
	elif Tearing.lower() == 'no':
		TearingInt = 0
	else:
		Tearing = input('Input not recognized for tearing, please retype. Y/N. ')
		conjunctivitisConversion()

def tuberculosisConversion(): #Tuberculosis' conversionto integers
	global Cough3WeeksInt
	global CoughBloodInt
	global ChestPainRespInt
	global WeightLossInt
	global FatigueInt
	global FeverInt
	global NightSweatsInt
	global ChillsInt
	global AppetiteLossInt

	global Cough3Weeks
	global CoughBlood
	global ChestPainResp
	global WeightLoss
	global Fatigue
	global Fever
	global NightSweats
	global Chills
	global AppetiteLoss

	if Cough3Weeks.lower() == 'y':
		Cough3WeeksInt = 1
	elif Cough3Weeks.lower() == 'yes':
		Cough3WeeksInt = 1
	elif Cough3Weeks.lower() == 'n':
		Cough3WeeksInt = 0
	elif Cough3Weeks.lower() == 'no':
		Cough3WeeksInt = 0
	else:
		Cough3Weeks = input('Input not recognized for coughing exceeding 3 weeks, please retype Y/N. ')
		tuberculosisConversion()
	if CoughBlood.lower() == 'y':
		CoughBloodInt = 1
	elif CoughBlood.lower() == 'yes':
		CoughBloodInt = 1
	elif CoughBlood.lower() == 'n':
		CoughBloodInt = 0
	elif CoughBlood.lower() == 'no':
		CoughBloodInt = 0
	else:
		CoughBlood = input('Input not recognize for coughing blood, please retype Y/N. ')
		tuberculosisConversion()
	if ChestPainResp.lower() == 'y':
		ChestPainRespInt = 1
	elif ChestPainResp.lower() == 'yes':
		ChestPainRespInt = 1
	elif ChestPainResp.lower() == 'n':
		ChestPainRespInt = 0
	elif ChestPainResp.lower() == 'no':
		ChestPainRespInt = 0
	else:
		ChestPainResp = input('Input not recognized for chest pain when breathing and coughing, please retype. Y/N. ')
		tuberculosisConversion()
	if WeightLoss.lower() == 'y':
		WeightLossInt = 1
	elif WeightLoss.lower() == 'yes':
		WeightLossInt = 1
	elif WeightLoss.lower() == 'n':
		WeightLossInt = 0
	elif WeightLoss.lower() == 'no':
		WeightLossInt = 0
	else:
		WeightLoss = input('Input not recognized for unintentional wieght loss, please retype. Y/N. ')
		tuberculosisConversion()
	if Fatigue.lower() == 'y':
		FatigueInt = 1
	elif Fatigue.lower() == 'yes':
		FatigueInt = 1
	elif Fatigue.lower() == 'n':
		FatigueInt = 0
	elif Fatigue.lower() == 'no':
		FatigueInt = 0
	else:
		Fatigue = input('Input not recognized for fatigue, please retype. Y/N. ')
		tuberculosisConversion()
	if Fever.lower() == 'y':
		FeverInt = 1
	elif Fever.lower() == 'yes':
		FeverInt = 1
	elif Fever.lower() == 'n':
		FeverInt = 0
	elif Fever.lower() == 'no':
		FeverInt = 0
	else:
		Fever = input('Input not recognized for a fever, please retype. Y/N. ')
		tuberculosisConversion()
	if NightSweats.lower() == 'y':
		NightSweatsInt = 1
	elif NightSweats.lower() == 'yes':
		NightSweatsInt = 1
	elif NightSweats.lower() == 'n':
		NightSweatsInt = 0
	elif NightSweats.lower() == 'no':
		NightSweatsInt = 0
	else:
		NightSweats = input('Input not recognized for sweating at night, please retype. Y/N. ')
		tuberculosisConversion()
	if Chills.lower() == 'y': #Sympt3
		ChillsInt = 1
	elif Chills.lower() == 'yes':
		ChillsInt = 1
	elif Chills.lower() == 'n':
		ChillsInt = 0
	elif Chills.lower() == 'no':
		ChillsInt = 0
	else:
		Chills = input('Input not recognized for chills, please retype. Y/N. ')
		tuberculosisConversion()
	if AppetiteLoss.lower() == 'y': #Sympt3
		AppetiteLossInt = 1
	elif AppetiteLoss.lower() == 'yes':
		AppetiteLossInt = 1
	elif AppetiteLoss.lower() == 'n':
		AppetiteLossInt = 0
	elif AppetiteLoss.lower() == 'no':
		AppetiteLossInt = 0
	else:
		AppetiteLoss = input('Input not recognized for appetite loss, please retype. Y/N. ')
		tuberculosisConversion()

def earInfectionConversion(): #An Ear Infection's conversion to integers
	global EaracheInt
	global EarFullInt
	global EarPainInt
	global MuffledHearInt
	global EarDrainInt

	global Earache
	global EarFull
	global EarPain
	global MuffledHear
	global EarDrain

	if Earache.lower() == 'y':
		EaracheInt = 1
	elif Earache.lower() == 'yes':
		EaracheInt = 1
	elif Earache.lower() == 'n':
		EaracheInt = 0
	elif Earache.lower() == 'no':
		EaracheInt = 0
	else:
		Earache = input('Input not recognized for an earache, please retype Y/N. ')
		earInfectionConversion()
	if EarFull.lower() == 'y':
		EarFullInt = 1
	elif EarFull.lower() == 'yes':
		EarFullInt = 1
	elif EarFull.lower() == 'n':
		EarFullInt = 0
	elif EarFull.lower() == 'no':
		EarFullInt = 0
	else:
		EarFull = input('Input not recognized for a feeling of fullness in the ear, please retype Y/N. ')
		earInfectionConversion()
	if EarPain.lower() == 'y':
		EarPainInt = 1
	elif EarPain.lower() == 'yes':
		EarPainInt = 1
	elif EarPain.lower() == 'n':
		EarPainInt = 0
	elif EarPain.lower() == 'no':
		EarPainInt = 0
	else:
		EarPain = input('Input not recognized for a sharp pain in the ear, please retype. Y/N. ')
		earInfectionConversion()
	if MuffledHear.lower() == 'y':
		MuffledHearInt = 1
	elif MuffledHear.lower() == 'yes':
		MuffledHearInt = 1
	elif MuffledHear.lower() == 'n':
		MuffledHearInt = 0
	elif MuffledHear.lower() == 'no':
		MuffledHearInt = 0
	else:
		MuffledHear = input('Input not recognized for muffled hearing, please retype. Y/N. ')
		earInfectionConversion()
	if EarDrain.lower() == 'y':
		EarDrainInt = 1
	elif EarDrain.lower() == 'yes':
		EarDrainInt = 1
	elif EarDrain.lower() == 'n':
		EarDrainInt = 0
	elif EarDrain.lower() == 'no':
		EarDrainInt = 0
	else:
		EarDrain = input('Input not recognized for ear drainage, please retype. Y/N. ')
		earInfectionConversion()

def myocaditusConversion(): #Myocaditus' conversion to integers
	global ChestPainInt
	global HeartArrythmiaInt
	global ShortnessOfBreathInt
	global LowAppendageSwellInt
	global FatigueInt
	global ViralInfectionInt

	global ChestPain
	global HeartArrythmia
	global ShortnessOfBreath
	global LowAppendageSwell
	global Fatigue
	global ViralInfection

	if ChestPain.lower() == 'y':
		ChestPainInt = 1
	elif ChestPain.lower() == 'yes':
		ChestPainInt = 1
	elif ChestPain.lower() == 'n':
		ChestPainInt = 0
	elif ChestPain.lower() == 'no':
		ChestPainInt = 0
	else:
		ChestPain = input('Input not recognized for chest pain, please retype Y/N. ')
		myocaditusConversion()
	if HeartArrythmia.lower() == 'y':
		HeartArrythmiaInt = 1
	elif HeartArrythmia.lower() == 'yes':
		HeartArrythmiaInt = 1
	elif HeartArrythmia.lower() == 'n':
		HeartArrythmiaInt = 0
	elif HeartArrythmia.lower() == 'no':
		HeartArrythmiaInt = 0
	else:
		HeartArrythmia = input('Input not recognized for heart arrythmia, please retype Y/N. ')
		myocaditusConversion()
	if ShortnessOfBreath.lower() == 'y':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'yes':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'n':
		ShortnessOfBreathInt = 0
	elif ShortnessOfBreath.lower() == 'no':
		ShortnessOfBreathInt = 0
	else:
		ShortnessOfBreath = input('Input not recognized for shortness of breath, please retype. Y/N. ')
		myocaditusConversion()
	if LowAppendageSwell.lower() == 'y':
		LowAppendageSwellInt = 1
	elif LowAppendageSwell.lower() == 'yes':
		LowAppendageSwellInt = 1
	elif LowAppendageSwell.lower() == 'n':
		LowAppendageSwellInt = 0
	elif LowAppendageSwell.lower() == 'no':
		LowAppendageSwellInt = 0
	else:
		LowAppendageSwell = input('Input not recognized for swelling in the the lower appendages, please retype. Y/N. ')
		myocaditusConversion()
	if Fatigue.lower() == 'y':
		FatigueInt = 1
	elif Fatigue.lower() == 'yes':
		FatigueInt = 1
	elif Fatigue.lower() == 'n':
		FatigueInt = 0
	elif Fatigue.lower() == 'no':
		FatigueInt = 0
	else:
		Fatigue = input('Input not recognized for fatigue, please retype. Y/N. ')
		myocaditusConversion()
	if ViralInfection.lower() == 'y':
		ViralInfectionInt = 1
	elif ViralInfection.lower() == 'yes':
		ViralInfectionInt = 1
	elif ViralInfection.lower() == 'n':
		ViralInfectionInt = 0
	elif ViralInfection.lower() == 'no':
		ViralInfectionInt = 0
	else:
		ViralInfection = input('Input not recognized for viral infection (headache, body aches, fever, sore throat, diarrhea), please retype. Y/N. ')
		myocaditusConversion()

def cardiomegalyConversion(): #Cardiomegaly's conversion to integers
	global AbdomenalSwellInt
	global HeartArrythmiaInt
	global ChestPainInt
	global CoughingInt
	global DizzinessInt
	global FatigueInt
	global ShortnessOfBreathInt
	global LowAppendageSwellInt

	global AbdomenalSwell
	global HeartArrythmia
	global ChestPain
	global Coughing
	global Dizziness
	global Fatigue
	global ShortnessOfBreath
	global LowAppendageSwell

	if AbdomenalSwell.lower() == 'y':
		AbdomenalSwellInt = 1
	elif AbdomenalSwell.lower() == 'yes':
		AbdomenalSwellInt = 1
	elif AbdomenalSwell.lower() == 'n':
		AbdomenalSwellInt = 0
	elif AbdomenalSwell.lower() == 'no':
		AbdomenalSwellInt = 0
	else:
		AbdomenalSwell = input('Input not recognized for abdominal bloating, please retype Y/N. ')
		cardiomegalyConversion()
	if HeartArrythmia.lower() == 'y':
		HeartArrythmiaInt = 1
	elif HeartArrythmia.lower() == 'yes':
		HeartArrythmiaInt = 1
	elif HeartArrythmia.lower() == 'n':
		HeartArrythmiaInt = 0
	elif HeartArrythmia.lower() == 'no':
		HeartArrythmiaInt = 0
	else:
		HeartArrythmia = input('Input not recognize for heart arrythmia, please retype Y/N. ')
		cardiomegalyConversion()
	if ChestPain.lower() == 'y':
		ChestPainInt = 1
	elif ChestPain.lower() == 'yes':
		ChestPainInt = 1
	elif ChestPain.lower() == 'n':
		ChestPainInt = 0
	elif ChestPain.lower() == 'no':
		ChestPainInt = 0
	else:
		ChestPain = input('Input not recognized for chest pain, please retype. Y/N. ')
		cardiomegalyConversion()
	if Coughing.lower() == 'y':
		CoughingInt = 1
	elif Coughing.lower() == 'yes':
		CoughingInt = 1
	elif Coughing.lower() == 'n':
		CoughingInt = 0
	elif Coughing.lower() == 'no':
		CoughingInt = 0
	else:
		Coughing = input('Input not recognized for coughing (especially when lying down), please retype. Y/N. ')
		cardiomegalyConversion()
	if Dizziness.lower() == 'y':
		DizzinessInt = 1
	elif Dizziness.lower() == 'yes':
		DizzinessInt = 1
	elif Dizziness.lower() == 'n':
		DizzinessInt = 0
	elif Dizziness.lower() == 'no':
		DizzinessInt = 0
	else:
		Dizziness = input('Input not recognized for dizziness, please retype. Y/N. ')
		cardiomegalyConversion()
	if Fatigue.lower() == 'y':
		FatigueInt = 1
	elif Fatigue.lower() == 'yes':
		FatigueInt = 1
	elif Fatigue.lower() == 'n':
		FatigueInt = 0
	elif Fatigue.lower() == 'no':
		FatigueInt = 0
	else:
		Fatigue = input('Input not recognized for fatigue, please retype. Y/N. ')
		cardiomegalyConversion()
	if ShortnessOfBreath.lower() == 'y':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'yes':
		ShortnessOfBreathInt = 1
	elif ShortnessOfBreath.lower() == 'n':
		ShortnessOfBreathInt = 0
	elif ShortnessOfBreath.lower() == 'no':
		ShortnessOfBreathInt = 0
	else:
		ShortnessOfBreath = input('Input not recognized for shortness of breath, please retype. Y/N. ')
		cardiomegalyConversion()
	if LowAppendageSwell.lower() == 'y':
		LowAppendageSwellInt = 1
	elif LowAppendageSwell.lower() == 'yes':
		LowAppendageSwellInt = 1
	elif LowAppendageSwell.lower() == 'n':
		LowAppendageSwellInt = 0
	elif LowAppendageSwell.lower() == 'no':
		LowAppendageSwellInt = 0
	else:
		LowAppendageSwell = input('Input not recognized for swelling in the the lower appendages, please retype. Y/N. ')
		cardiomegalyConversion()

def Diagnose(): #This function prints all the information the doctor may need to properly diagnose a patient.
	if AilmentQuery.lower() == 'lrti': #Stands for Lower Respiratory Tract Infection
		LRTIDiagnose()
	elif AilmentQuery.lower() == 'the flu':
		theFluDiagnose()
	elif AilmentQuery.lower() == 'conjunctivitis': #Pink Eye
		conjunctivitisDiagnose()
	elif AilmentQuery.lower() == 'tuberculosis':
		tuberculosisDiagnose()
	elif AilmentQuery.lower() == 'ear infection':
		earInfectionDiagnose()
	elif AilmentQuery.lower() == 'myocaditus':
		myocaditusDiagnose()
	elif AilmentQuery.lower() == 'cardiomegaly':
		cardiomegalyDiagnose()
	elif AilmentQuery.lower() == 'idk' or AilmentQuery.lower() == "i don't know":
		IDKDiagnose()
	if AddSym.lower() == 'no':
		print('The patient provided no additional symptoms')
	else:
		print('The patient provided these additional symptoms: ' + AddSym)

def LRTIDiagnose(): #I tested and the code works comepletely, no syntax errors or other issues, please use it as an example.
	global ShortnessOfBreathInt
	global WeaknessInt
	global FeverInt
	global CoughingInt
	global FatigueInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0

	LRTIMax = '5'
	LRTITrue = ShortnessOfBreathInt + WeaknessInt + FeverInt + CoughingInt + FatigueInt
	print('The patient believes they are suffering ' + str(LRTITrue) + '/' + LRTIMax + ' symptoms of Lower Respiratory Tract Infection.')
	if ShortnessOfBreathInt == 1: #Sets the amount of shared symptoms actually shared
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		SST = True
	if FatigueInt == 1:
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		tuberculosisTrue = FatigueInt + FeverInt + CoughingInt
		tuberculosisMax = '9'
		SST = True
	if FeverInt == 1:
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		tuberculosisTrue = FeverInt + FatigueInt
		tuberculosisMax = '9'
		SST = True
	if CoughingInt == 1:
		FluTrue = CoughingInt + FeverInt + FatigueInt
		FluMax = '8'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		SST = True
	if SST == True:
		print('Some symptoms match other symptom sets. The Ailment scores are:')
		if myocaditusTrue > 0:
			print('Myocaditus ' + str(myocaditusTrue) + '/' + myocaditusMax)
		if cardiomegalyTrue > 0:
			print('Cardiomegaly ' + str(cardiomegalyTrue) + '/' + cardiomegalyMax)
		if FluTrue > 0:
			print('The Flu ' + str(FluTrue) + '/' + FluMax)
		if tuberculosisTrue > 0:
			print('Tuberculosis ' + str(tuberculosisTrue) + '/' + tuberculosisMax)


def theFluDiagnose():
	global SoreThroatInt
	global RunnyStuffyNoseInt
	global MuscleBodyAchesInt
	global HeadachesInt
	global VomitingAndDiahrreaInt
	global FeverInt
	global CoughingInt
	global FatigueInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	FluMax = '8'
	FluTrue = FeverInt + CoughingInt + SoreThroatInt + RunnyStuffyNoseInt + MuscleBodyAchesInt + HeadachesInt + FatigueInt + VomitingAndDiahrreaInt 
	print('The patient believes they are suffering ' + str(FluTrue) + '/' + FluMax + ' symptoms of The Flue')

	if FatigueInt == 1:
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		LRTITrue = FeverInt + CoughingInt + FatigueInt
		LRTIMax = '5'
		tuberculosisTrue = FatigueInt + FeverInt + CoughingInt
		tuberculosisMax = '9'
		SST = True
	if FeverInt == 1:
		LRTITrue = FeverInt + CoughingInt + FatigueInt
		LRTIMax = '5'
		tuberculosisTrue = FeverInt + FatigueInt
		tuberculosisMax = '9'
		SST = True
	if CoughingInt == 1:
		LRTITrue = CoughingInt + FeverInt + FatigueInt
		LRTIMax = '5'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		SST = True
	if SST == True:
		print('Some symptoms match other symptom sets. The Ailment scores are:')
		if myocaditusTrue > 0:
			print('Myocaditus ' + str(myocaditusTrue) + '/' + myocaditusMax)
		if cardiomegalyTrue > 0:
			print('Cardiomegaly ' + str(cardiomegalyTrue) + '/' + cardiomegalyMax)
		if LRTITrue > 0:
			print('Lower Respiratory Tract Infection ' + str(LRTITrue) + '/' + LRTIMax)
		if tuberculosisTrue > 0:
			print('Tuberculosis ' + str(tuberculosisTrue) + '/' + tuberculosisMax)


def conjunctivitisDiagnose():
	global RedEyesInt
	global IcthyEyesInt
	global GrittyEyesInt
	global CrustyEyesInt
	global TearingInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	conjunctivitisMax = '5'
	conjunctivitisTrue = RedEyesInt + IcthyEyesInt + GrittyEyesInt + CrustyEyesInt + TearingInt
	print('The patient believes they are suffering' + str(conjunctivitisTrue) + '/' + conjunctivitisMax + 'symptoms of Conjunctivitis')

def tuberculosisDiagnose():
	global Cough3WeeksInt
	global CoughBloodInt
	global ChestPainRespInt
	global WeightLossInt
	global NightSweatsInt
	global ChillsInt
	global AppetiteLossInt
	global FeverInt
	global FatigueInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	tuberculosisMax = '9'
	tuberculosis = Cough3WeeksInt + CoughBloodInt + ChestPainRespInt + WeightLossInt + FatigueInt + FeverInt + NightSweatsInt + ChillsInt + AppetiteLossInt
	print('The patient believes they are suffering' + str(tuberculosisTrue) + '/' + tuberculosisMax + 'symptoms of Tuberculosis')

	if FatigueInt == 1:
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		LRTITrue = FatigueInt + FeverInt + CoughingInt
		LRTIMax = '9'
		SST = True
	if FeverInt == 1:
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		LRTITrue = FeverInt + FatigueInt
		LRTIMax = '5'
		SST = True
	if SST == True:
		print('Some symptoms match other symptom sets. The Ailment scores are:')
		if myocaditusTrue > 0:
			print('Myocaditus ' + str(myocaditusTrue) + '/' + myocaditusMax)
		if cardiomegalyTrue > 0:
			print('Cardiomegaly ' + str(cardiomegalyTrue) + '/' + cardiomegalyMax)
		if FluTrue > 0:
			print('The Flu ' + str(FluTrue) + '/' + FluMax)
		if LRTITrue > 0:
			print('Lower Respiratory Tract Infection ' + str(LRTITrue) + '/' + LRTIMax)


def earInfectionDiagnose():
	global EaracheInt
	global EarFullInt
	global EarPainInt
	global MuffledHearInt
	global EarDrainInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	earInfectionMax = '5' 
	earInfectionTrue = EaracheInt + EarFullInt + EarPainInt + MuffledHearInt + EarDrainInt 
	print('The patient believes they are suffering' + str(earInfectionTrue) + '/' + earInfectionMax + 'symptoms of an Ear Infection')

def myocaditusDiagnose():
	global ChestPainInt
	global HeartArrythmiaInt
	global LowAppendageSwellInt
	global ViralInfectionInt
	global ShortnessOfBreathInt
	global FatigueInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	myocaditusMax = '6'
	myocaditusTrue = ChestPainInt + HeartArrythmiaInt + ShortnessOfBreathInt + LowAppendageSwellInt + FatigueInt + ViralInfectionInt
	print('The patient believes they are suffering' + str(myocaditusTrue) + '/' + myocaditusMax + 'symptoms of Myocaditus')

	if ShortnessOfBreathInt == 1: #Sets the amount of shared symtoms actually shared
		LRTITrue = ShortnessOfBreathInt + FatigueInt
		LRTIMax = '5'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		SST = True
	if FatigueInt == 1:
		LRTITrue = ShortnessOfBreathInt + FatigueInt
		LRTIMax = '5'
		cardiomegalyTrue = ShortnessOfBreathInt + FatigueInt
		cardiomegalyMax = '8'
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		tuberculosisTrue = FatigueInt + FeverInt + CoughingInt
		tuberculosisMax = '9'
		SST = True
	if SST == True:
		print('Some symptoms match other symptom sets. The Ailment scores are:')
		if LRTITrue > 0:
			print('Lower Respiratory Tract Infection ' + str(LRTITrue) + '/' + LRTIMax)
		if cardiomegalyTrue > 0:
			print('Cardiomegaly ' + str(cardiomegalyTrue) + '/' + cardiomegalyMax)
		if FluTrue > 0:
			print('The Flu ' + str(FluTrue) + '/' + FluMax)
		if tuberculosisTrue > 0:
			print('Tuberculosis ' + str(tuberculosisTrue) + '/' + tuberculosisMax)


def cardiomegalyDiagnose():
	global AbdomenalSwellInt
	global HeartArrythmiaInt
	global ChestPainInt
	global CoughingInt
	global DizzinessInt
	global LowAppendageSwellInt
	global ShortnessOfBreathInt
	global FatigueInt
	global LRTITrue
	global LRTIMax
	global FluTrue
	global FluMax
	global conjunctivitisTrue
	global conjunctivitisMax
	global tuberculosisTrue
	global tuberculosisMax
	global earInfectionTrue
	global earInfectionMax
	global myocaditusTrue
	global myocaditusMax
	global cardiomegalyTrue
	global cardiomegalyMax
	global SST

	SST = False
	FluTrue = 0
	conjunctivitisTrue = 0
	tuberculosisTrue = 0
	earInfectionTrue = 0
	myocaditusTrue = 0
	cardiomegalyTrue = 0
	
	cardiomegalyMax = '8'
	cardiomegalyTrue = AbdomenalSwellInt + HeartArrythmiaInt + ChestPainInt + CoughingInt + DizzinessInt + FatigueInt + ShortnessOfBreathInt + LowAppendageSwellInt
	print('The patient believes they are suffering' + str(cardiomegalyTrue) + '/' + cardiomegalyMax + 'symptoms of Cardiomegaly')

	if ShortnessOfBreathInt == 1: #Sets the amount of shared symtoms actually shared
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		LRTITrue = ShortnessOfBreathInt + FatigueInt
		LRTIMax = '5'
		SST = True
	if FatigueInt == 1:
		myocaditusTrue = ShortnessOfBreathInt + FatigueInt
		myocaditusMax = '6'
		LRTITrue = ShortnessOfBreathInt + FatigueInt
		LRTIMax = '5'
		FluTrue = FeverInt + CoughingInt + FatigueInt
		FluMax = '8'
		tuberculosisTrue = FatigueInt + FeverInt + CoughingInt
		tuberculosisMax = '9'
		SST = True
	if CoughingInt == 1:
		FluTrue = CoughingInt + FeverInt + FatigueInt
		FluMax = '8'
		LRTITrue = ShortnessOfBreathInt + FatigueInt
		LRTIMax = '5'
		SST = True
	if SST == True:
		print('Some symptoms match other symptom sets. The Ailment scores are:')
		if myocaditusTrue > 0:
			print('Myocaditus ' + str(myocaditusTrue) + '/' + myocaditusMax)
		if LRTITrue > 0:
			print('Lower Respiratory Tract Infection ' + str(LRTITrue) + '/' + LRTIMax)
		if FluTrue > 0:
			print('The Flu ' + str(FluTrue) + '/' + FluMax)
		if tuberculosisTrue > 0:
			print('Tuberculosis ' + str(tuberculosisTrue) + '/' + tuberculosisMax)

getPatientInputInitial()
convertToInteger()
Diagnose()