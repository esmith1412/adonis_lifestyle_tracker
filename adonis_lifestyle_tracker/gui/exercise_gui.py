'''
Contains the functions needed to add and update exercise information in the database,
using a GUI.
'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.common import DB_PATH, get_sorted_tuple
from adonis_lifestyle_tracker.exercise import (
    add_equipment,
    add_exercise,
    add_exercise_to_week,
    get_equipment,
    get_resistance,
    change_resistance
)


sg.theme('Reddit')

LABEL_SIZE = (10, 1)
INPUT_SIZE = (28, 1)
BUTTON_SIZE = (18, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')

WEEKS = get_sorted_tuple(DB_PATH, 'week', 'week_exercise')
EQUIPMENT = get_sorted_tuple(DB_PATH, 'id', 'equipment')
EXERCISES = get_sorted_tuple(DB_PATH, 'id', 'exercise')
REPS = get_sorted_tuple(DB_PATH, 'reps', 'week_exercise')
RESISTANCE = get_sorted_tuple(DB_PATH, 'resistance', 'week_exercise')

layout = [
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( WEEKS, key='-WEEK-', size=(6, 1) )],
    [sg.T('Exercise', size=LABEL_SIZE), sg.InputCombo(EXERCISES, key='-EXERCISE-', size=INPUT_SIZE)],
    [sg.T('Equipment', size=LABEL_SIZE), sg.InputCombo(EQUIPMENT, key='-EQUIPMENT-', size=(INPUT_SIZE))],
    [sg.T('Reps', size=LABEL_SIZE), sg.InputCombo( REPS, key='-REPS-', size=(6, 1) )],
    [sg.T('Resistance', size=LABEL_SIZE), sg.InputCombo( RESISTANCE, key='-RESISTANCE-', size=(6, 1) )],
    [
        sg.B('Add Equipment', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
    ],
    [
        sg.B('Get Equipment', size=BUTTON_SIZE),
        sg.B('Get Resistance', size=BUTTON_SIZE),
        sg.B('Change Resistance', size=BUTTON_SIZE, button_color=CHANGE_BUTTON_COLOR)
    ]
]

window = sg.Window('Exercise Manager', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    if event == 'Add Equipment':
        equipment = values['-EQUIPMENT-'].strip()

        if equipment:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add the '{equipment}' equipment to the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(add_equipment(DB_PATH, equipment), title='Message')
                window['-EQUIPMENT-'].update('')
                window['-EQUIPMENT-'].update( values=get_sorted_tuple(DB_PATH, 'id', 'equipment') )
        else:
            sg.popup_error('You must provide equipment!', title='Error')

    elif event == 'Add Exercise':
        exercise = values['-EXERCISE-'].strip()
        equipment = values['-EQUIPMENT-'].strip()

        if exercise and equipment:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add the '{exercise}' exercise with "
                f"the '{equipment}' equipment to the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(add_exercise(DB_PATH, exercise, equipment), title='Message')
                window['-EXERCISE-'].update('')
                window['-EQUIPMENT-'].update('')
                window['-EXERCISE-'].update( values=get_sorted_tuple(DB_PATH, 'id', 'exercise') )
        else:
            sg.popup_error(
                'You must provide an exercise and its equipment!',
                title='Error'
            )

    elif event == 'Add Exercise to Week':

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        resistance = values['-RESISTANCE-'].strip()

        if exercise and resistance:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add the '{exercise}' exercise with "
                f"the '{reps}' reps and '{resistance}' resistance to week {week} in the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    add_exercise_to_week(DB_PATH, week, exercise, reps, resistance),
                    title='Message'
                )

                # To clear the input fields
                window['-WEEK-'].update('')
                window['-EXERCISE-'].update('')
                window['-REPS-'].update('')
                window['-RESISTANCE-'].update('')

                # To add the new information to the dropdowns
                window['-WEEK-'].update( values=get_sorted_tuple(DB_PATH, 'week', 'week_exercise') )
                window['-REPS-'].update( values=get_sorted_tuple(DB_PATH, 'reps', 'week_exercise') )
                window['-RESISTANCE-'].update( values=get_sorted_tuple(DB_PATH, 'resistance', 'week_exercise') )
        else:
            sg.popup_error(
                'You must provide an exercise and resistance!', title='Error'
            )

    elif event == 'Change Resistance':

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        new_resistance = values['-RESISTANCE-'].strip()

        if exercise and new_resistance:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to update the resistance for week {week}, "
                f"the '{exercise}' exercise, and {reps} reps to '{new_resistance}' in the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    change_resistance(DB_PATH, week, exercise, reps, new_resistance),
                    title='Message'
                )

                # To clear the input fields
                window['-WEEK-'].update('')
                window['-EXERCISE-'].update('')
                window['-REPS-'].update('')
                window['-RESISTANCE-'].update('')

                window['-RESISTANCE-'].update( values=get_sorted_tuple(DB_PATH, 'resistance', 'week_exercise') )
        else:
            sg.popup_error(
                'You must provide an exercise and resistance!', title='Error'
            )

    elif event == 'Get Resistance':

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        if exercise and reps:
            sg.popup(
                get_resistance(DB_PATH, week, exercise, reps),
                title='Message'
            )
        else:
            sg.popup_error(
                'You must provide an exercise and number of reps!', title='Error'
            )

    elif event == 'Get Equipment':
        exercise = values['-EXERCISE-'].strip()

        if exercise:
            sg.popup( get_equipment(DB_PATH, exercise), title='Message' )
        else:
            sg.popup_error('You must provide an exercise!', title='Error')

    else:
        continue

window.close()
