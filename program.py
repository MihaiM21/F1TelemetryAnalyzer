import customtkinter
from Quali.Throttle_comparison import ThrottleComp
from Quali.plot_qualifying_results import QualiResults
from Quali.top_speed_plot import TopSpeedFunc
from Race.plot_strategy import StrategyFunc
from Quali.Track_comparison import TrackCompFunc
from Quali.plot_speed_traces import SpeedTraceFunc
from Race.plot_team_pace_ranking import TeamPaceRankingFunc
from Race.plot_driver_laptimes import DriverLaptimesFunc
from Race.plot_laptimes_distribution import LaptimesDistributionFunc

def ShowFrame():
    # Showing the input for drivers and teams for some scripts that require it
    if selectedPlot.get() == "Drivers track comparison" or selectedPlot.get() == "Speed Trace(2 drivers)" or selectedPlot.get() == "Driver Laptimes":
        if selectedPlot.get() == "Drivers track comparison" or selectedPlot.get() == "Speed Trace(2 drivers)":
            labelD1.pack(pady=10, padx=20)
            entryDriverOne.pack(pady=10, padx=20)
            labelT1.pack(pady=10, padx=20)
            entryTeamOne.pack(pady=10, padx=20)
            labelD2.pack(pady=10, padx=20)
            entryDriverTwo.pack(pady=10, padx=20)
            labelT2.pack(pady=10, padx=20)
            entryTeamTwo.pack(pady=10, padx=20)
        elif selectedPlot.get() == "Driver Laptimes":
            labelD1.pack(pady=10, padx=20)
            entryDriverOne.pack(pady=10, padx=20)

    elif selectedPlot.get() != 'Drivers track comparison' and selectedPlot.get() != "Speed Trace(2 drivers)":
        entryDriverOne.forget()
        entryTeamOne.forget()
        entryDriverTwo.forget()
        entryTeamTwo.forget()
        labelD1.forget()
        labelT1.forget()
        labelD2.forget()
        labelT2.forget()

    # Show the "Execute" Button only if there is selected a specific race
    if selectedPlot.get() != '' and selectedYear.get() != '' and selectedEvent.get() != '' and selectedRound.get() != '':
        confirmButton.pack(pady=20, padx=20)
    labelForQ.forget()
    labelForQFP.forget()


def runFile():
    ShowFrame
    if selectedPlot.get() == 'Throttle comparison' and (
            selectedEvent.get() == 'SQ' or selectedEvent.get() == 'Q' or selectedEvent.get() == 'FP1' or selectedEvent.get() == 'FP2' or selectedEvent.get() == 'FP3'):
        ThrottleComp(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get())
    elif selectedPlot.get() == "Throttle comparison" and (
            selectedEvent.get() != 'SQ' or selectedEvent.get() != 'Q' and selectedEvent.get() != 'FP1' and selectedEvent.get() != 'FP2' and selectedEvent.get() != 'FP3'):
        labelForQFP.pack(pady=20, padx=20)

    if selectedPlot.get() == 'Qualifying Results' and (selectedEvent.get() == 'SQ' or selectedEvent.get() == "Q" or selectedEvent.get() == 'FP1' or selectedEvent.get() == 'FP2' or selectedEvent.get() == 'FP3'):
        QualiResults(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get())
    elif selectedPlot.get() == "Qualifying Results" and (selectedEvent.get() != 'SQ' or selectedEvent.get() != 'Q'):
        labelForQ.pack(pady=20, padx=20)

    if selectedPlot.get() == 'Top Speed' and (
            selectedEvent.get() == 'SQ' or selectedEvent.get() == 'Q' or selectedEvent.get() == 'FP1' or selectedEvent.get() == 'FP2' or selectedEvent.get() == 'FP3'):
        TopSpeedFunc(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get())
    elif selectedPlot.get() == "Top Speed" and (
            selectedEvent.get() != 'SQ' or selectedEvent.get() != 'Q' and selectedEvent.get() != 'FP1' and selectedEvent.get() != 'FP2' and selectedEvent.get() != 'FP3'):
        labelForQFP.pack(pady=20, padx=20)

    if selectedPlot.get() == 'Strategy' and (selectedEvent.get() == 'R' or selectedEvent.get() == 'S'):
        StrategyFunc(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get())

    if selectedPlot.get() == 'Drivers track comparison' and (
            selectedEvent.get() == 'SQ' or selectedEvent.get() == 'Q' or selectedEvent.get() == 'FP1' or selectedEvent.get() == 'FP2' or selectedEvent.get() == 'R' or selectedEvent.get() == 'FP3'):
        TrackCompFunc(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get(), entryDriverOne.get(),
                      entryDriverTwo.get(), entryTeamOne.get(), entryTeamTwo.get())
        
    elif selectedPlot.get() == "Drivers track comparison" and (
            selectedEvent.get() != 'SQ' or selectedEvent.get() != 'Q' and selectedEvent.get() != 'FP1' and selectedEvent.get() != 'FP2' and selectedEvent.get() != 'FP3'):
        labelForQFP.pack(pady=20, padx=20)

    if selectedPlot.get() == 'Speed Trace(2 drivers)' and (
            selectedEvent.get() == 'SQ' or selectedEvent.get() == 'Q' or selectedEvent.get() == 'FP1' or selectedEvent.get() == 'FP2' or selectedEvent.get() == 'FP3'):
        SpeedTraceFunc(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get(), entryDriverOne.get(),
                       entryDriverTwo.get(), entryTeamOne.get(), entryTeamTwo.get())
    elif selectedPlot.get() == "Speed Trace(2 drivers)" and (
            selectedEvent.get() != 'SQ' or selectedEvent.get() != 'Q' and selectedEvent.get() != 'FP1' and selectedEvent.get() != 'FP2' and selectedEvent.get() != 'FP3'):
        labelForQFP.pack(pady=20, padx=20)

    if selectedPlot.get() == "Team Pace" and (selectedEvent.get() == 'S' or selectedEvent.get() == "R"):
        TeamPaceRankingFunc(int(selectedYear.get()), int(selectedRound.get()), selectedEvent.get())

    if selectedPlot.get() == "Drivers laptimes distribution" and selectedEvent.get() == 'R':
        LaptimesDistributionFunc(selectedYear.get(), selectedRound.get(), selectedEvent.get())

    if selectedPlot.get() == "Driver Laptimes" and selectedEvent.get() == 'R':
        DriverLaptimesFunc(selectedYear.get(),selectedRound.get(), selectedEvent.get(),entryDriverOne.get())

    confirmButton.forget()
    entryDriverOne.forget()
    entryTeamOne.forget()
    entryDriverTwo.forget()
    entryTeamTwo.forget()
    labelD1.forget()
    labelT1.forget()
    labelD2.forget()
    labelT2.forget()


customtkinter.set_appearance_mode("dark")

# Setting the current year and making a list of years to choose from 2000 till present
year_list = []
x = 2015
while x <= 2024:
    year_list.append(str(x))
    x = x + 1


# Setting the rounds
rounds = list()
x = 1
while x <= 24:
    rounds.append(str(x))
    x = x + 1

# File names that user can select
file_names = ["Throttle comparison",
              "Qualifying Results",
              "Top Speed",
              "Strategy",
              "Drivers track comparison",
              "Speed Trace(2 drivers)",
              "Team Pace",
              "Drivers laptimes distribution",
              "Driver Laptimes"]
event_type = ["FP1", "FP2", "FP3", "SQ", "S", "Q", "R"]

# Creating window
root = customtkinter.CTk()
root.title("Formula One Telemetry Graphs")

root.geometry("1280x720")

# Creating frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="none", expand=False)

# Frame for selected driver info and team information
frame2 = customtkinter.CTkFrame(master=frame, height=70)
frame2.pack(pady=5, padx=10, fill='both', expand=False, side="right")

# Creating frames for every options menu
f1 = customtkinter.CTkFrame(master=frame)
f1.pack(pady=5, padx=5)
f2 = customtkinter.CTkFrame(master=frame)
f2.pack(pady=5, padx=5)
f3 = customtkinter.CTkFrame(master=frame)
f3.pack(pady=5, padx=5)
f4 = customtkinter.CTkFrame(master=frame)
f4.pack(pady=5, padx=5)

# Options menu for scrips
selectPlotText = customtkinter.CTkLabel(master=f1, text="Select plot:", justify="center")
selectedPlot = customtkinter.StringVar(master=f1)
Options = customtkinter.CTkOptionMenu(master=f1, values=file_names, variable=selectedPlot , width=200)
selectPlotText.pack(padx=1, pady=1)
Options.pack(pady=10, padx=10)

# Options menu for years
selectedYear = customtkinter.StringVar(master=f2)
selectYearText = customtkinter.CTkLabel(master=f2, text='Select year:')
yearOptions = customtkinter.CTkOptionMenu(master=f2, values=year_list, variable=selectedYear, width=200)
selectYearText.pack(padx=1, pady=1)
yearOptions.pack(pady=10, padx=10)

# Options menu for round number
selectedRound = customtkinter.StringVar(master=f3)
selectRoundNumberText = customtkinter.CTkLabel(master=f3, text='Select race number:')
roundOptions = customtkinter.CTkOptionMenu(master=f3, values=rounds, variable=selectedRound, width=200)
selectRoundNumberText.pack(padx=1, pady=1)
roundOptions.pack(pady=10, padx=10)

# Options menu for event type
selectedEvent = customtkinter.StringVar(master=f4)
selectEventText = customtkinter.CTkLabel(master=f4, text='Select event:')
eventOptions = customtkinter.CTkOptionMenu(master=f4, values=event_type, variable=selectedEvent, width=200)
selectEventText.pack(padx=1, pady=1)
eventOptions.pack(pady=10, padx=10)

# Select Button
button = customtkinter.CTkButton(master=frame, text="Select", command=ShowFrame, text_color="black")
button.pack(pady=10, padx=10)

# Confirm/Execute button
confirmButton = customtkinter.CTkButton(master=frame2, text="EXECUTE", command=runFile)

# Driver inputs for some scrips who need it
entryDriverOne = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter driver 1 acronim")
entryTeamOne = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter team 1 acronim")
entryDriverTwo = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter driver 2 acronim")
entryTeamTwo = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter team 2 acronim")
labelD1 = customtkinter.CTkLabel(master=frame2, text="Driver 1:")
labelT1 = customtkinter.CTkLabel(master=frame2, text="Team 1:")
labelD2 = customtkinter.CTkLabel(master=frame2, text="Driver 2:")
labelT2 = customtkinter.CTkLabel(master=frame2, text="Team 2:")

# Label with you must select a certain event type
labelForQ = customtkinter.CTkLabel(master=frame2, text="You must select Q")
labelForQFP = customtkinter.CTkLabel(master=frame2, text="You must select Q, FP1, FP2 or FP3")

root.mainloop()
