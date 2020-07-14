import PySimpleGUI as sg

def clear():
    window.FindElement('-OUT-').Update('') #clears the dialog box

#A dictionary of bodies
bodies={
"LEO" :"9000 - 9400m/s.",
"GTO" : """2500m/s.
1450m/s to circularise.
+ 450m/s to 0 out inclinatination from Cape.""",
"Moon" : """3120m/s TLI.
140m/s capture, 800m/s total for low orbit.
1720 MINIMUM for landing and ascent.""",

"Mercury" : """5550m/s.
6310m/s capture + 1220m/s for low orbit.
3060m/s to land.""",
"Venus" : """3490m/s.
360m/s capture + 2940m/s for low orbit.
Non-propulsive landing. 27000m/s ascent to orbit.""",

"Mars" : """3600m/s.
670m/s capture + 1440m/s for low orbit.
400 - 800m/s landing w/parachute.
3600m/s ascent to orbit.""",
"Deimos" : """Figures assume elliptical Mars orbit (minimum-energy capture).
340m/s transfer. 660m/s capture into low orbit.
4m/s to land.""",
"Phobos" : """Figures assume elliptical Mars orbit (minimum-energy capture).
740m/s transfer. 550m/s capture into low orbit.
6m/s to land.""",

"Vesta" : """4520m/s.
4110m/s capture + 100m/s for low orbit.
160m/s to land.""",
"Ceres" : """4900m/s.
4390m/s capture + 150m/s for low orbit.
270m/s to land.""",

"Jupiter" : """6300m/s.
270m/s capture + 17480m/s for low orbit.
Non-propulsive descent.""",
"Himalia" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
190m/s transfer. 2870m/s capture + 20m/s for low orbit.
40m/s to land.""",
"Callisto" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
1120m/s transfer. 4100m/s capture + 700m/s for low orbit.
1750m/s to land.""",
"Ganymede" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
1920m/s transfer. 4790m/s capture + 790m/s for low orbit.
1950m/s to land.""",
"Europa" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
2980m/s transfer. 5920m/s capture + 580m/s for low orbit.
1440m/s to land.""",
"Io" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
4540m/s transfer. 5790m/s capture + 730m/s for low orbit.
1780m/s to land.""",
"Amalthea" : """Figures assume elliptical Jupiter orbit (minimum-energy capture).
9190m/s transfer. 6310m/s capture + 10m/s for low orbit.
20m/s to land.""",

"Saturn" : """7290m/s.
420m/s capture + 10220m/s for low orbit.
Non-propulsive descent.""",
"Iapetus" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
300m/s transfer. 2160m/s capture + 160m/s for low orbit.
410m/s to land.""",
"Titan" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
860m/s transfer. 2200m/s capture + 660m/s for low orbit.
Non-propulsive descent. 7600m/s ascent to orbit.""",
"Rhea" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
1900m/s tranfer. 4010m/s capture + 180m/s for low orbit.
450m/s to land.""",
"Dione" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
2570m/s transfer. 4230m/s capture + 140m/s for low orbit.
360m/s to land.""",
"Tethys" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
3190m/s transfer. 4290m/s capture + 110m/s for low orbit.
270m/s to land.""",
"Enceladus" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
3830m/s transfer. 4270m/s capture + 70m/s for low orbit.
160m/s to land.""",
"Mimas" : """Figures assume elliptical Saturn orbit (minimum-energy capture).
4700m/s transfer. 4020m/s capture + 40m/s for low orbit.
100m/s to land.""",


"Uranus" : """7980m/s.
510m/s capture + 6130m/s for low orbit.
Non-propulsive descent.""",
"Oberon" : """Figures assume elliptical Uranus orbit (minimum-energy capture).
460m/s transfer. 1630m/s capture + 210m/s for low orbit.
530m/s to land.""",
"Titania" : """Figures assume elliptical Uranus orbit (minimum-energy capture).
610m/s transfer. 1780m/s capture + 220m/s for low orbit.
560m/s to land.""",
"Umbriel" : """Figures assume elliptical Uranus orbit (minimum-energy transfer).
970m/s transfer. 2240m/s capture + 150m/s for low orbit.
370m/s to land.""",
"Ariel" : """Figures assume elliptical Uranus orbit (minimum-energy capture).
1320m/s transfer. 2310m/s capture + 160m/s for low orbit.
390m/s to land.""",
"Miranda" : """Figures assume elliptical Uranus orbit (minimum-energy transfer).
1870m/s transfer. 2610m/s capture + 50m/s for low orbit.
130m/s to land.""",

"Neptune" : """8250m/s.
350m/s capture + 6750m/s for low orbit.
Non-propulsive descent.""",
"Nereid" : """Figures assume elliptical Neptune orbit (minimum-energy transfer).
50m/s transfer. 870m/s capture + 40m/s for low orbit.
90m/s to land.""",
"Triton" : """Figures assume elliptical Neptune orbit (minimum-energy transfer).
790m/s transfer. 1710m/s capture + 410m/s for low orbit.
1050m/s to land.""",
"Proteus" : """Figures assume elliptical Neptune orbit (minimum-energy transfer).
2170m/s transfer. 2900m/s capture + 50m/s for low orbit.
110m/s to land.""",

"Pluto" : """8360m/s.
2700m/s capture + 350m/s for low orbit.
890m/s to land.""",
"Charon" : """Figures assume elliptical Pluto orbit (minimum-energy capture).
40m/s transfer. 20m/s capture + 160m/s for low orbit.
420m/s to land."""
}


# ****GUI SHIT****
sg.theme("DarkBlue")
layout = [[sg.T("INNER PLANETS:")],
          [sg.T("Earth-Moon system")],
          [sg.B("LEO"), sg.B("GTO"), sg.B("Moon")],
          [sg.T("Innermost planets")],
          [sg.B("Mercury"), sg.B("Venus")],
          [sg.T("Martian system")],
          [sg.B("Mars"), sg.B("Deimos"), sg.B("Phobos")],
          [sg.T("Minor planets")],
          [sg.B("Ceres"), sg.B("Vesta")],
          [sg.T("OUTER PLANETS:")],
          [sg.T("Jovian system")],
          [sg.B("Jupiter"), sg.B("Himalia"), sg.B("Callisto"), sg.B("Ganymede"), sg.B("Europa"), sg.B("Io"), sg.B("Amalthea")],
          [sg.T("Saturnian system")],
          [sg.B("Saturn"), sg.B("Iapetus"), sg.B("Titan"), sg.B("Rhea"), sg.B("Dione"), sg.B("Tethys"), sg.B("Enceladus"), sg.B("Mimas")],
          [sg.T("Uranian System")],
          [sg.B("Uranus"), sg.B("Oberon"), sg.B("Titania"), sg.B("Umbriel"), sg.B("Ariel"), sg.B("Miranda")],
          [sg.T("Neptunian system")],
          [sg.B("Neptune"), sg.B("Nereid"), sg.B("Triton"), sg.B("Proteus")],
          [sg.T("Plutonian system")],
          [sg.B("Pluto"), sg.B("Charon")],
          [sg.T("")],
          [sg.Output(key='-OUT-', size=(200,5))]]

window = sg.Window("", layout, alpha_channel=0.95, size=(500, 700), icon="titleIconBLUE.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event: #if there is an event
        clear() #clear the dialog box
        print(bodies[event]) #print from the dictionary the relevant bodies' info
