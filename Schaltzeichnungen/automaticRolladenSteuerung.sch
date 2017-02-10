EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:RelaisDoppelRaspberry
LIBS:automaticRolladenSteuerung-cache
LIBS:rolladenmotor
LIBS:steckdose
LIBS:taster
LIBS:usbraspberrystromadapter
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Raspberry_Pi_2_3 U1
U 1 1 58937801
P 2600 3650
F 0 "U1" H 3300 2400 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2200 4550 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20" H 3600 4900 50  0001 C CNN
F 3 "" H 2650 3500 50  0001 C CNN
	1    2600 3650
	1    0    0    -1  
$EndComp
$Comp
L Relais U2
U 1 1 589378E8
P 5250 2000
F 0 "U2" H 5300 2000 60  0000 C CNN
F 1 "Relais" H 5250 1350 60  0000 C CNN
F 2 "" H 5600 2100 60  0001 C CNN
F 3 "" H 5600 2100 60  0001 C CNN
	1    5250 2000
	1    0    0    -1  
$EndComp
NoConn ~ 4700 1700
NoConn ~ 4700 1800
$Comp
L +5V #PWR3
U 1 1 589384EE
P 4700 2450
F 0 "#PWR3" H 4700 2300 50  0001 C CNN
F 1 "+5V" H 4700 2590 50  0000 C CNN
F 2 "" H 4700 2450 50  0000 C CNN
F 3 "" H 4700 2450 50  0000 C CNN
	1    4700 2450
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR2
U 1 1 58938650
P 4700 2150
F 0 "#PWR2" H 4700 1900 50  0001 C CNN
F 1 "GND" H 4700 2000 50  0000 C CNN
F 2 "" H 4700 2150 50  0000 C CNN
F 3 "" H 4700 2150 50  0000 C CNN
	1    4700 2150
	0    1    1    0   
$EndComp
$Comp
L GND #PWR1
U 1 1 58938741
P 4700 1900
F 0 "#PWR1" H 4700 1650 50  0001 C CNN
F 1 "GND" H 4700 1750 50  0000 C CNN
F 2 "" H 4700 1900 50  0000 C CNN
F 3 "" H 4700 1900 50  0000 C CNN
	1    4700 1900
	0    1    1    0   
$EndComp
$Comp
L taster U4
U 1 1 589388E3
P 5250 6250
F 0 "U4" H 5300 6600 60  0000 C CNN
F 1 "taster" H 5350 6000 60  0000 C CNN
F 2 "" H 5350 6250 60  0001 C CNN
F 3 "" H 5350 6250 60  0001 C CNN
	1    5250 6250
	1    0    0    -1  
$EndComp
$Comp
L RolladenMotor U8
U 1 1 589389BA
P 8000 1250
F 0 "U8" H 8000 1500 60  0000 C CNN
F 1 "RolladenMotor" H 8000 650 60  0000 C CNN
F 2 "" H 8000 1250 60  0001 C CNN
F 3 "" H 8000 1250 60  0001 C CNN
	1    8000 1250
	1    0    0    -1  
$EndComp
$Comp
L Steckdose U6
U 1 1 589389FB
P 7850 3700
F 0 "U6" H 7900 3950 60  0000 C CNN
F 1 "Steckdose" H 7900 3300 60  0000 C CNN
F 2 "" H 7750 3350 60  0001 C CNN
F 3 "" H 7750 3350 60  0001 C CNN
	1    7850 3700
	1    0    0    -1  
$EndComp
$Comp
L Steckdose U7
U 1 1 58939200
P 7900 5500
F 0 "U7" H 7950 5750 60  0000 C CNN
F 1 "Steckdose" H 7950 5100 60  0000 C CNN
F 2 "" H 7800 5150 60  0001 C CNN
F 3 "" H 7800 5150 60  0001 C CNN
	1    7900 5500
	1    0    0    -1  
$EndComp
$Comp
L USBRaspberryStromAdapter U3
U 1 1 58939297
P 5250 3700
F 0 "U3" H 5200 4000 60  0000 C CNN
F 1 "USBRaspberryStromAdapter" H 5300 3350 60  0000 C CNN
F 2 "" H 5100 3550 60  0001 C CNN
F 3 "" H 5100 3550 60  0001 C CNN
	1    5250 3700
	1    0    0    -1  
$EndComp
Text Label 8300 7650 0    60   ~ 0
02.02.2017
Text Label 7450 7500 0    60   ~ 0
Intelligente-Sonnen-Rolladensteuerung
Text Label 8650 7750 0    60   ~ 0
Max-Wolfgang-Aigner
Text Label 10700 7650 0    60   ~ 0
1.0.0
$Comp
L taster U5
U 1 1 5893B26D
P 5250 7050
F 0 "U5" H 5300 7400 60  0000 C CNN
F 1 "taster" H 5350 6800 60  0000 C CNN
F 2 "" H 5350 7050 60  0001 C CNN
F 3 "" H 5350 7050 60  0001 C CNN
	1    5250 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 3900 8300 4600
Wire Wire Line
	8300 4600 6950 4600
Wire Wire Line
	6950 4600 6950 5700
Wire Wire Line
	6950 5700 7550 5700
Wire Wire Line
	8350 3750 8500 3750
Wire Wire Line
	8500 3750 8500 4750
Wire Wire Line
	8500 4750 7050 4750
Wire Wire Line
	7050 4750 7050 5550
Wire Wire Line
	7050 5550 7500 5550
Wire Wire Line
	8300 3600 8650 3600
Wire Wire Line
	8650 3600 8650 4850
Wire Wire Line
	8650 4850 7200 4850
Wire Wire Line
	7200 4850 7200 5400
Wire Wire Line
	7200 5400 7550 5400
Wire Wire Line
	7500 3600 6600 3600
Wire Wire Line
	6600 3600 6600 3700
Wire Wire Line
	6600 3700 5800 3700
Wire Wire Line
	5800 3550 6950 3550
Wire Wire Line
	6950 3550 6950 3750
Wire Wire Line
	6950 3750 7450 3750
Wire Wire Line
	7500 3900 5800 3900
Wire Wire Line
	5800 3900 5800 3850
Wire Wire Line
	4950 3700 4050 3700
Wire Wire Line
	4050 3700 4050 4650
Wire Wire Line
	4050 4650 3400 4650
Wire Wire Line
	7350 3900 7350 1650
Wire Wire Line
	7350 1650 7400 1650
Connection ~ 7350 3900
Wire Wire Line
	7150 3750 7150 1900
Wire Wire Line
	7150 1900 5850 1900
Connection ~ 7150 3750
Wire Wire Line
	5850 2150 6950 2150
Wire Wire Line
	6950 2150 6950 1350
Wire Wire Line
	6950 1350 7400 1350
Wire Wire Line
	7400 1200 6850 1200
Wire Wire Line
	6850 1200 6850 1750
Wire Wire Line
	6850 1750 5850 1750
Wire Wire Line
	4700 2250 4000 2250
Wire Wire Line
	4000 2250 4000 2750
Wire Wire Line
	4000 2750 3500 2750
Wire Wire Line
	4700 2350 4100 2350
Wire Wire Line
	4100 2350 4100 2850
Wire Wire Line
	4100 2850 3500 2850
Wire Wire Line
	3500 2950 4450 2950
Wire Wire Line
	4450 2950 4450 6150
Wire Wire Line
	4450 6150 4900 6150
Wire Wire Line
	2900 4950 2900 6300
Wire Wire Line
	2900 6300 4900 6300
Wire Wire Line
	3500 3150 4350 3150
Wire Wire Line
	4350 3150 4350 6950
Wire Wire Line
	4350 6950 4900 6950
Wire Wire Line
	4900 7100 2800 7100
Wire Wire Line
	2800 7100 2800 4950
Wire Wire Line
	7400 1500 7250 1500
Wire Wire Line
	7250 1500 7250 3600
Connection ~ 7250 3600
Wire Wire Line
	5850 2300 6750 2300
Wire Wire Line
	6750 2300 6750 3550
Connection ~ 6750 3550
Text Label 7550 6100 0    60   ~ 0
vorhandene_Steckdose
$EndSCHEMATC
