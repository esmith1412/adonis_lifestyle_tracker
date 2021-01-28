'''
Contains the handler functions to manage the nutrition information
in the manager GUI.
'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import get_sorted_tuple
from adonis_lifestyle_tracker.nutrition.add_nutrition import *
from adonis_lifestyle_tracker.nutrition.get_nutrition import *
from adonis_lifestyle_tracker.nutrition.update_nutrition import *
from adonis_lifestyle_tracker.nutrition.delete_nutrition import *


def handle_add_food(window, values, db_path=None):
    '''Handles the event for adding a new food to the database.'''
    food = values['-FOOD-'].strip()

    try:
        calories = int(values['-KCAL-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the calories!', title='Error'
        )
        return

    try:
        protein = int(values['-PROTEIN-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the grams of protein!', title='Error'
        )
        return

    if food and calories and protein and protein >= 0:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the food '{food}' to the database, "
            f"with {calories} calories and {protein} grams of protein?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                add_food(db_path, food, calories, protein), title='Message'
            )

            window['-FOOD-'].update('')
            window['-KCAL-'].update('')
            window['-PROTEIN-'].update('')

            window['-FOOD-'].update(
                values=get_sorted_tuple(db_path, 'id', 'food')
            )


def handle_add_weekly_totals(window, values, db_path=None):
    '''
    Handles the event for adding a new week with its total calories
    and protein to the database.
    '''
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the week!', title='Error'
        )
        return

    try:
        calories = int(values['-KCAL-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the calories!', title='Error'
        )
        return

    try:
        protein = int(values['-PROTEIN-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the grams of protein!', title='Error'
        )
        return

    confirmation = sg.popup_yes_no(
        f"Are you sure you want to add week {week}, with {calories} "
        f"total calories and {protein} total grams of protein?",
        title='Confirmation'
    )

    if confirmation == 'Yes':
        sg.popup(
            add_weekly_totals(db_path, week, calories, protein),
            title='Message'
        )

        window['-WEEK-'].update('')
        window['-KCAL-'].update('')
        window['-PROTEIN-'].update('')

        window['-WEEK-'].update(
            values=get_sorted_tuple(db_path, 'id', 'week')
        )


def handle_add_weekly_food(window, values, db_path=None):
    '''Handles the event to add a food to a given week.'''
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the week!', title='Error'
        )
        return

    food = values['-FOOD-'].strip()

    if food:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the food '{food}' "
            f"to week {week} in the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                add_weekly_food(db_path, week, food), title='Message'
            )

            window['-WEEK-'].update('')
            window['-FOOD-'].update('')

    else:
        sg.popup_error('You must enter a food and choose a day!', title='Error')


def handle_get_food(values, db_path=None):
    '''
    Handles the event to display the calories and protein for the
    specified food.
    '''
    food = values['-FOOD-'].strip()

    if food:
        sg.popup(get_food(db_path, food), title='Message')
    else:
        sg.popup_error('You must enter a food!', title='Error')


def handle_get_calories_left(values, db_path=None):
    '''
    Handles the event to get the number of calories left to consume
    for a given week.
    '''
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the week!', title='Error'
        )
    else:
        sg.popup(get_calories_left(db_path, week), title='Message')


def handle_get_protein_left(values, db_path=None):
    '''
    Handles the event to get the number of grams of protein left to consume
    for a given week.
    '''
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the week!',
            title='Error'
        )
    else:
        sg.popup(get_protein_left(db_path, week), title='Message')


def handle_update_food(window, values, db_path=None):
    '''Handles the event to update the calories and/or protein for the specified food.'''
    food = values['-FOOD-'].strip()

    try:
        calories = int(values['-KCAL-'])
    except ValueError:
        calories = None

    try:
        protein = int(values['-PROTEIN-'])
    except ValueError:
        protein = None

    if food and calories and not protein:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the calories for food '{food}' to {calories}?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                update_food(db_path, food, calories=calories), title='Message'
            )

            window['-FOOD-'].update('')
            window['-KCAL-'].update('')

    elif food and not calories and protein and protein >= 0:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the grams of protein for food '{food}' to {protein}?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                update_food(db_path, food, protein=protein), title='Message'
            )

            window['-FOOD-'].update('')
            window['-PROTEIN-'].update('')

    elif food and calories and protein and protein >= 0:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the calories for food '{food}' "
            f"to {calories}, and its grams of protein to {protein}?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                update_food(db_path, food, calories=calories, protein=protein),
                title='Message'
            )

            window['-FOOD-'].update('')
            window['-KCAL-'].update('')
            window['-PROTEIN-'].update('')

    elif food and not calories and not protein:
        sg.popup_error(
            'You must enter the calories and/or protein for the food!',
            title='Error'
        )
    else:
        sg.popup_error('You must enter a food!', title='Error')


def handle_delete_food(window, values, db_path=None):
    '''Handles the event to delete the specified food from the database.'''
    food = values['-FOOD-'].strip()

    if food:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete the food '{food}' from the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_food(db_path, food), title='Message')

            window['-FOOD-'].update('')

            window['-FOOD-'].update(
                values=get_sorted_tuple(db_path, 'id', 'food')
            )


def handle_delete_week(window, values, db_path=None):
    '''Handles the event to delete a week from the database.'''
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error(
            'You must provide a number for the week!', title='Error'
        )
    else:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete week {week} from the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_week(db_path, week), title='Message')

            window['-WEEK-'].update('')

            window['-WEEK-'].update(
                values=get_sorted_tuple(db_path, 'id', 'week')
            )
