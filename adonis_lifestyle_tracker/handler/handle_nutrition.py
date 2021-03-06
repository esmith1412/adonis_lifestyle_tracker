import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import get_sorted_tuple
from adonis_lifestyle_tracker.nutrition.add_nutrition import *
from adonis_lifestyle_tracker.nutrition.get_nutrition import *
from adonis_lifestyle_tracker.nutrition.update_nutrition import *
from adonis_lifestyle_tracker.nutrition.delete_nutrition import *


def handle_add_food(window, values, db_path):
    food = values['-FOOD-'].strip()

    try:
        calories = int(values['-KCAL-'])
    except ValueError:
        sg.popup_error('You must provide a number for the calories!', title='Error')
    else:
        try:
            protein = int(values['-PROTEIN-'])
        except ValueError:
            sg.popup_error('You must provide a number for the grams of protein!', title='Error')
        else:
            if food and calories > 0 and protein >= 0:
                confirmation = sg.popup_yes_no(
                    f"Are you sure you want to add the food '{food}' to the database, "
                    f"with {calories} calories and {protein} grams of protein?",
                    title='Confirmation'
                )

                if confirmation == 'Yes':
                    sg.popup(add_food(db_path, food, calories, protein), title='Message')
                    window['-FOOD-'].update('')
                    window['-KCAL-'].update('')
                    window['-PROTEIN-'].update('')
                    window['-FOOD-'].update(values=get_sorted_tuple(db_path, 'id', 'food'))


def handle_add_total_calories_and_protein_for_week(window, values, db_path):
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error('You must provide a number for the week!', title='Error')
    else:
        try:
            calories = int(values['-KCAL-'])
        except ValueError:
            sg.popup_error('You must provide a number for the calories!', title='Error')
        else:
            try:
                protein = int(values['-PROTEIN-'])
            except ValueError:
                sg.popup_error('You must provide a number for the grams of protein!', title='Error')
            else:
                confirmation = sg.popup_yes_no(
                    f"Are you sure you want to add week {week}, with {calories} "
                    f"total calories and {protein} total grams of protein?",
                    title='Confirmation'
                )

                if calories > 0 and protein > 0 and confirmation == 'Yes':
                    sg.popup(add_total_calories_and_protein_for_week(db_path, week, calories, protein), title='Message')
                    window['-WEEK-'].update('')
                    window['-KCAL-'].update('')
                    window['-PROTEIN-'].update('')
                    window['-WEEK-'].update(values=get_sorted_tuple(db_path, 'id', 'week'))


def handle_add_food_to_week(window, values, db_path):
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error('You must provide a number for the week!', title='Error')
    else:
        food = values['-FOOD-'].strip()

        if food:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add the food '{food}' to week {week} in the database?", title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(add_food_to_week(db_path, week, food), title='Message')
                window['-WEEK-'].update('')
                window['-FOOD-'].update('')

        else:
            sg.popup_error('You must enter a food and choose a day!', title='Error')


def handle_get_calories_and_protein_for_food(values, db_path):
    food = values['-FOOD-'].strip()

    if food:
        sg.popup(get_calories_and_protein_for_food(db_path, food), title='Message')
    else:
        sg.popup_error('You must enter a food!', title='Error')


def handle_get_calories_left_for_week(values, db_path):
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error('You must provide a number for the week!', title='Error')
    else:
        sg.popup(get_calories_left_for_week(db_path, week), title='Message')


def handle_get_protein_left_for_week(values, db_path):
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error('You must provide a number for the week!', title='Error')
    else:
        sg.popup(get_protein_left_for_week(db_path, week), title='Message')


def handle_update_calories_and_protein_for_food(window, values, db_path):
    food = values['-FOOD-'].strip()

    try:
        calories = int(values['-KCAL-'])
    except ValueError:
        calories = None

    try:
        protein = int(values['-PROTEIN-'])
    except ValueError:
        protein = None

    if food and calories > 0 and not protein:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the calories for food '{food}' to {calories}?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(update_food(db_path, food, calories=calories), title='Message')
            window['-FOOD-'].update('')
            window['-KCAL-'].update('')

    elif food and not calories and protein >= 0:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the grams of protein for food '{food}' to {protein}?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(update_food(db_path, food, protein=protein), title='Message')
            window['-FOOD-'].update('')
            window['-PROTEIN-'].update('')

    elif food and calories > 0 and protein >= 0:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the calories for food '{food}' "
            f"to {calories}, and its grams of protein to {protein}?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(update_food(db_path, food, calories=calories, protein=protein), title='Message')
            window['-FOOD-'].update('')
            window['-KCAL-'].update('')
            window['-PROTEIN-'].update('')

    elif food and not calories and not protein:
        sg.popup_error('You must enter the calories and/or protein for the food!', title='Error')
    else:
        sg.popup_error('You must enter a food!', title='Error')


def handle_delete_food(window, values, db_path):
    food = values['-FOOD-'].strip()

    if food:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete the food '{food}' from the database?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_food(db_path, food), title='Message')
            window['-FOOD-'].update('')
            window['-FOOD-'].update(values=get_sorted_tuple(db_path, 'id', 'food'))

    else:
        sg.popup_error('You must enter a food!', title='Error')


def handle_delete_week(window, values, db_path):
    try:
        week = int(values['-WEEK-'])
    except ValueError:
        sg.popup_error('You must provide a number for the week!', title='Error')
    else:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete week {week} from the database?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_week(db_path, week), title='Message')
            window['-WEEK-'].update('')
            window['-WEEK-'].update(values=get_sorted_tuple(db_path, 'id', 'week'))
