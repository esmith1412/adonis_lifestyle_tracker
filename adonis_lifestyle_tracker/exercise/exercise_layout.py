"""Contains the PySimpleGUI layout for the Adonis Lifestyle Tracker exercise GUI."""
import PySimpleGUI as sg


sg.theme('Reddit')

NUTRITION_LABEL_SIZE = (7, 1)
EXERCISE_LABEL_SIZE = (10, 1)
TEXT_INPUT_SIZE = (42, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (16, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')
DELETE_BUTTON_COLOR = ('black', '#ff4040')

layout = [
    [
        sg.T('Equipment', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EQUIPMENT-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Exercise', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EXERCISE-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Reps', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo((3, 5, 6, 7, 8, 10, 12, 13, 15, 21), key='-REPS-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Resistance', size=EXERCISE_LABEL_SIZE),
        sg.I(key='-RESISTANCE-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.B(
            'Add Equipment',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new piece of workout equipment to the database.'
        ),
        sg.B(
            'Get Equipment',
            size=BUTTON_SIZE,
            tooltip='Display the equipment for the specified exercise.'
        ),
        sg.B(
            'Update Equipment',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the equipment for the specified exercise.'
        )
    ],
    [
        sg.B(
            'Add Exercise',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new exercise to the database, and chooses its equipment.'
        ),
        sg.B(
            'Get Resistance',
            size=BUTTON_SIZE,
            tooltip='Displays the resistance for the specified exercise and rep range.'
        ),
        sg.B(
            'Update Resistance',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the resistance for the specified exercise and rep range.'
        )
    ],
    [
        sg.B(
            'Delete Equipment',
            size=(27, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified equipment from the database.',
            pad=(5, 0)
        ),
        sg.B(
            'Delete Exercise',
            size=(27, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified exercise and its equipment from the database.',
            pad=(1, 0)
        ),
    ],
    [sg.Frame('Database Path', layout=[
        [
            sg.I(key='-PATH-', enable_events=True, size=(32, 1)),
            sg.FileBrowse(),
            sg.Button('Load Database', button_color=('white', '#8a2be2'))
        ]
    ])]
]
