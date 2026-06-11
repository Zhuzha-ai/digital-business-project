import customtkinter as ctk
import csv
import os
from tkinter import messagebox


# SETTINGS

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# DESIGN-KONSTANTEN

APP_BG = "#F3F5F0"
CARD_BG = "white"
BUTTON_COLOR = "#A8C3A0"
BUTTON_HOVER = "#8FAE87"
RESET_COLOR = "#D98C8C"
RESET_HOVER = "#C76F6F"
TEXT_COLOR = "#2B2B2B"


# DATEIEN

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_FILE = os.path.join(BASE_DIR, "orders.csv")
FEEDBACK_FILE = os.path.join(BASE_DIR, "feedback.csv")
PROFILE_FILE = os.path.join(BASE_DIR, "user_profile.csv")


# GLOBALE VARIABLEN

user_profile = {}
selected_dish = None


# GERICHTE DES WOCHENPLANS

schedule = {
    "Monday": [
        {
            "name": "Chicken Bowl",
            "category": "Normal",
            "price": 4.90,
            "weight": 450,
            "kcal": 650,
            "protein": 42,
            "carbs": 51,
            "fat": 14,
            "allergens": "Gluten, Soy, Sesame",
            "score": "8.4 / 10",
            "micros": {
                "Fiber": "8 g",
                "Iron": "3.2 mg",
                "Calcium": "120 mg",
                "Magnesium": "95 mg",
                "Vitamin C": "35 mg"
            }
        },
        {
            "name": "Salmon Rice",
            "category": "Normal",
            "price": 5.90,
            "weight": 480,
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish",
            "score": "8.2 / 10",
            "micros": {
                "Fiber": "6 g",
                "Iron": "2.1 mg",
                "Calcium": "85 mg",
                "Magnesium": "110 mg",
                "Vitamin D": "8 µg"
            }
        },
        {
            "name": "Vegan Lentil Curry",
            "category": "Vegan",
            "price": 4.20,
            "weight": 500,
            "kcal": 590,
            "protein": 24,
            "carbs": 82,
            "fat": 16,
            "allergens": "Celery, Mustard",
            "score": "8.6 / 10",
            "micros": {
                "Fiber": "15 g",
                "Iron": "5.4 mg",
                "Calcium": "140 mg",
                "Magnesium": "135 mg",
                "Vitamin C": "42 mg"
            }
        }
    ],

    "Tuesday": [
        {
            "name": "Beef Potato Plate",
            "category": "Normal",
            "price": 5.40,
            "weight": 520,
            "kcal": 720,
            "protein": 39,
            "carbs": 68,
            "fat": 30,
            "allergens": "Milk, Celery",
            "score": "7.6 / 10",
            "micros": {
                "Fiber": "7 g",
                "Iron": "4.8 mg",
                "Calcium": "160 mg",
                "Magnesium": "90 mg",
                "Vitamin B12": "2.8 µg"
            }
        },
        {
            "name": "Turkey Couscous Bowl",
            "category": "Normal",
            "price": 4.80,
            "weight": 460,
            "kcal": 630,
            "protein": 38,
            "carbs": 74,
            "fat": 18,
            "allergens": "Gluten",
            "score": "8.0 / 10",
            "micros": {
                "Fiber": "9 g",
                "Iron": "3.5 mg",
                "Calcium": "95 mg",
                "Magnesium": "105 mg",
                "Vitamin C": "30 mg"
            }
        },
        {
            "name": "Vegan Chickpea Pasta",
            "category": "Vegan",
            "price": 4.10,
            "weight": 470,
            "kcal": 610,
            "protein": 27,
            "carbs": 88,
            "fat": 13,
            "allergens": "Gluten",
            "score": "8.3 / 10",
            "micros": {
                "Fiber": "13 g",
                "Iron": "4.9 mg",
                "Calcium": "115 mg",
                "Magnesium": "120 mg",
                "Vitamin C": "25 mg"
            }
        }
    ],

    "Wednesday": [
        {
            "name": "Pasta Napoli",
            "category": "Vegetarian",
            "price": 3.90,
            "weight": 430,
            "kcal": 610,
            "protein": 20,
            "carbs": 108,
            "fat": 11,
            "allergens": "Gluten, Milk",
            "score": "7.5 / 10",
            "micros": {
                "Fiber": "7 g",
                "Iron": "2.7 mg",
                "Calcium": "180 mg",
                "Magnesium": "75 mg",
                "Vitamin C": "28 mg"
            }
        },
        {
            "name": "Vegetarian Chili",
            "category": "Vegetarian",
            "price": 4.00,
            "weight": 500,
            "kcal": 580,
            "protein": 25,
            "carbs": 76,
            "fat": 15,
            "allergens": "Celery",
            "score": "8.1 / 10",
            "micros": {
                "Fiber": "14 g",
                "Iron": "4.5 mg",
                "Calcium": "130 mg",
                "Magnesium": "125 mg",
                "Vitamin C": "50 mg"
            }
        },
        {
            "name": "Vegan Tofu Rice Bowl",
            "category": "Vegan",
            "price": 4.30,
            "weight": 480,
            "kcal": 640,
            "protein": 31,
            "carbs": 78,
            "fat": 20,
            "allergens": "Soy, Sesame",
            "score": "8.7 / 10",
            "micros": {
                "Fiber": "10 g",
                "Iron": "4.2 mg",
                "Calcium": "260 mg",
                "Magnesium": "145 mg",
                "Vitamin C": "38 mg"
            }
        }
    ],

    "Thursday": [
        {
            "name": "Chicken Teriyaki Rice",
            "category": "Normal",
            "price": 4.90,
            "weight": 470,
            "kcal": 680,
            "protein": 41,
            "carbs": 80,
            "fat": 18,
            "allergens": "Soy, Sesame",
            "score": "8.0 / 10",
            "micros": {
                "Fiber": "6 g",
                "Iron": "2.9 mg",
                "Calcium": "100 mg",
                "Magnesium": "105 mg",
                "Vitamin C": "32 mg"
            }
        },
        {
            "name": "Fish Potato Bowl",
            "category": "Normal",
            "price": 5.50,
            "weight": 500,
            "kcal": 660,
            "protein": 36,
            "carbs": 62,
            "fat": 24,
            "allergens": "Fish, Mustard",
            "score": "7.9 / 10",
            "micros": {
                "Fiber": "7 g",
                "Iron": "2.2 mg",
                "Calcium": "95 mg",
                "Magnesium": "115 mg",
                "Vitamin D": "6 µg"
            }
        },
        {
            "name": "Vegan Sweet Potato Stew",
            "category": "Vegan",
            "price": 4.20,
            "weight": 510,
            "kcal": 560,
            "protein": 19,
            "carbs": 84,
            "fat": 14,
            "allergens": "Celery",
            "score": "8.5 / 10",
            "micros": {
                "Fiber": "12 g",
                "Iron": "3.8 mg",
                "Calcium": "125 mg",
                "Magnesium": "115 mg",
                "Vitamin A": "850 µg"
            }
        }
    ],

    "Friday": [
        {
            "name": "Cheese Spaetzle Bowl",
            "category": "Vegetarian",
            "price": 4.30,
            "weight": 480,
            "kcal": 720,
            "protein": 26,
            "carbs": 90,
            "fat": 28,
            "allergens": "Gluten, Milk, Egg",
            "score": "7.2 / 10",
            "micros": {
                "Fiber": "5 g",
                "Iron": "2.4 mg",
                "Calcium": "320 mg",
                "Magnesium": "80 mg",
                "Vitamin B12": "1.4 µg"
            }
        },
        {
            "name": "Vegetarian Falafel Plate",
            "category": "Vegetarian",
            "price": 4.40,
            "weight": 490,
            "kcal": 650,
            "protein": 23,
            "carbs": 72,
            "fat": 25,
            "allergens": "Sesame, Gluten",
            "score": "8.0 / 10",
            "micros": {
                "Fiber": "11 g",
                "Iron": "4.0 mg",
                "Calcium": "170 mg",
                "Magnesium": "130 mg",
                "Vitamin C": "34 mg"
            }
        },
        {
            "name": "Vegan Buddha Bowl",
            "category": "Vegan",
            "price": 4.50,
            "weight": 460,
            "kcal": 600,
            "protein": 22,
            "carbs": 79,
            "fat": 19,
            "allergens": "Soy, Sesame",
            "score": "8.8 / 10",
            "micros": {
                "Fiber": "13 g",
                "Iron": "4.6 mg",
                "Calcium": "210 mg",
                "Magnesium": "155 mg",
                "Vitamin C": "45 mg"
            }
        }
    ]
}


# HILFSFUNKTIONEN

def show_output(title, text):
    details_title.configure(text=title)

    details_textbox.configure(state="normal")
    details_textbox.delete("1.0", "end")
    details_textbox.insert("1.0", text)
    details_textbox.configure(state="disabled")



def ensure_csv_file(file_path, header):
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)


def file_exists_with_data(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) > 0


def save_user_profile_to_file():
    with open(PROFILE_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Weight", "Goal"])
        writer.writerow([
            user_profile["weight"],
            user_profile["goal"]
        ])


def load_user_profile_from_file():
    global user_profile

    if not file_exists_with_data(PROFILE_FILE):
        return

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            weight = row.get("Weight", "").strip()
            goal = row.get("Goal", "").strip()



def rating_to_stars(rating):
    full_stars = int(round(rating))
    empty_stars = 5 - full_stars
    return "★" * full_stars + "☆" * empty_stars


def create_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER,
        text_color="black"
    )


def format_micronutrients(micros):
    text = ""

    for nutrient, value in micros.items():
        text += f"{nutrient}: {value}\n"

    return text


def get_fiber_value(dish):
    fiber_text = dish["micros"].get("Fiber", "0 g")
    fiber_number = fiber_text.replace("g", "").strip()

    try:
        return float(fiber_number)
    except ValueError:
        return 0


def get_personal_recommendation(dish):
    if not user_profile:
        return (
            "Personal Recommendation:\n"
            "Create a user profile to receive a personal recommendation."
        )

    goal = user_profile.get("goal", "")

    kcal = dish["kcal"]
    protein = dish["protein"]
    fat = dish["fat"]
    fiber = get_fiber_value(dish)

    recommendation_score = 0
    reasons = []

    if goal == "Build Muscle":
        if protein >= 35:
            recommendation_score += 2
            reasons.append("high protein content")
        elif protein >= 25:
            recommendation_score += 1
            reasons.append("moderate protein content")

        if kcal >= 600:
            recommendation_score += 1
            reasons.append("enough energy for muscle building")

        if fat <= 30:
            recommendation_score += 1
            reasons.append("balanced fat content")

    elif goal == "Lose Weight":
        if kcal <= 620:
            recommendation_score += 2
            reasons.append("moderate calorie content")
        elif kcal <= 680:
            recommendation_score += 1
            reasons.append("still acceptable calorie content")

        if protein >= 25:
            recommendation_score += 1
            reasons.append("supports satiety through protein")

        if fiber >= 10:
            recommendation_score += 1
            reasons.append("high fiber content for better satiety")

        if fat <= 20:
            recommendation_score += 1
            reasons.append("moderate fat content")

    elif goal == "Maintain Weight":
        if 580 <= kcal <= 700:
            recommendation_score += 2
            reasons.append("balanced calorie amount")

        if protein >= 22:
            recommendation_score += 1
            reasons.append("solid protein amount")

        if fiber >= 7:
            recommendation_score += 1
            reasons.append("good fiber content")

        if fat <= 28:
            recommendation_score += 1
            reasons.append("balanced fat content")

    if recommendation_score >= 4:
        result = "Highly recommended"
    elif recommendation_score >= 2:
        result = "Recommended"
    else:
        result = "Less suitable"

    reasons_text = ""

    for reason in reasons:
        reasons_text += f"- {reason}\n"

    if reasons_text == "":
        reasons_text = "- does not strongly match the selected goal\n"

    return (
        f"Personal Recommendation:\n"
        f"Goal: {goal}\n"
        f"Result: {result}\n\n"
        f"Reasons:\n"
        f"{reasons_text}"
    )


# USER PROFILE

def open_profile_window():
    new_window = ctk.CTkToplevel(root)
    new_window.title("User Profile")
    new_window.geometry("400x430")
    new_window.grab_set()

    weight_label = ctk.CTkLabel(
        new_window,
        text="Weight in kg",
        font=("Arial", 18)
    )
    weight_label.pack(pady=(20, 5))

    weight_entry = ctk.CTkEntry(
        new_window,
        placeholder_text="e.g. 70"
    )
    weight_entry.pack()

    goal_label = ctk.CTkLabel(
        new_window,
        text="Goal",
        font=("Arial", 18)
    )
    goal_label.pack(pady=(20, 5))

    goal_option = ctk.CTkOptionMenu(
        new_window,
        values=["Build Muscle", "Lose Weight", "Maintain Weight"]
    )
    goal_option.pack()

    if user_profile:
        weight_entry.insert(0, user_profile["weight"])
        goal_option.set(user_profile["goal"])

    def save_profile():
        global user_profile

        weight = weight_entry.get().strip()

        if weight == "":
            show_output("User Profile", "Please enter your weight.")
            return

        try:
            float(weight)
        except ValueError:
            show_output("User Profile", "Please enter a valid weight.")
            return

        user_profile = {
            "weight": weight,
            "goal": goal_option.get()
        }

        save_user_profile_to_file()

        show_output(
            "User Profile",
            f"Profile saved successfully!\n\n"
            f"Weight: {user_profile['weight']} kg\n"
            f"Goal: {user_profile['goal']}"
        )

        new_window.destroy()


    save_button = create_button(
        new_window,
        "Save Profile",
        save_profile
    )
    save_button.pack(pady=25)


# GERICHTE

def new_dishes(day=None):
    for widget in dishes_frame.winfo_children():
        widget.destroy()

    chosen_day = weekday.get()

    for dish in schedule[chosen_day]:
        button_text = f"{dish['name']} | {dish['category']} | {dish['price']:.2f} €"

        button = ctk.CTkButton(
            dishes_frame,
            text=button_text,
            height=50,
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER,
            text_color="black",
            command=lambda d=dish: show_dish(d)
        )
        button.pack(fill="x", padx=20, pady=10)


def show_dish(dish):
    global selected_dish
    selected_dish = dish

    micronutrients_text = format_micronutrients(dish["micros"])
    personal_recommendation = get_personal_recommendation(dish)

    text = (
        f"Name: {dish['name']}\n"
        f"Category: {dish['category']}\n"
        f"Price: {dish['price']:.2f} €\n"
        f"Weight: {dish['weight']} g\n\n"
        f"Calories: {dish['kcal']} kcal\n"
        f"Protein: {dish['protein']} g\n"
        f"Carbs: {dish['carbs']} g\n"
        f"Fat: {dish['fat']} g\n\n"
        f"Micronutrients:\n"
        f"{micronutrients_text}\n"
        f"Allergens: {dish['allergens']}\n\n"
        f"Health Score: {dish['score']}\n\n"
        f"{personal_recommendation}"
    )

    if user_profile.get("goal") == "Build Muscle":
        try:
            weight = float(user_profile["weight"])
            protein_goal = weight * 2
            protein_percent = round(dish["protein"] / protein_goal * 100)

            if protein_percent >= 25:
                text += (
                    f"\n\nProtein Coverage: {protein_percent}%"
                    f"\nRecommended for muscle gain."
                )
            else:
                text += f"\n\nProtein Coverage: {protein_percent}%"

        except ValueError:
            text += "\n\nPlease enter a valid weight in your profile."

    show_output("Dish Details", text)


# BESTELLUNG SPEICHERN

def order_dish():
    if selected_dish is None:
        show_output("Order", "Please select a dish first.")
        return

    ensure_csv_file(
        ORDERS_FILE,
        ["Dish", "Category", "Price", "Amount", "Day"]
    )

    with open(ORDERS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            selected_dish["name"],
            selected_dish["category"],
            selected_dish["price"],
            1,
            weekday.get()
        ])

    show_output(
        "Order",
        f"Order saved successfully!\n\n"
        f"Dish: {selected_dish['name']}\n"
        f"Category: {selected_dish['category']}\n"
        f"Price: {selected_dish['price']:.2f} €\n"
        f"Day: {weekday.get()}"
    )


# FEEDBACK SPEICHERN

def save_feedback():
    if selected_dish is None:
        show_output("Feedback", "Please select a dish first.")
        return

    rating = int(round(slider.get()))
    comment = comment_box.get("1.0", "end").strip()

    if comment == "":
        show_output("Feedback", "Please enter a feedback comment.")
        return

    ensure_csv_file(
        FEEDBACK_FILE,
        ["Dish", "Category", "Price", "Rating", "Comment"]
    )

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            selected_dish["name"],
            selected_dish["category"],
            selected_dish["price"],
            rating,
            comment
        ])

    comment_box.delete("1.0", "end")

    stars = rating_to_stars(rating)

    show_output(
        "Feedback",
        f"Feedback saved successfully!\n\n"
        f"Dish: {selected_dish['name']}\n"
        f"Category: {selected_dish['category']}\n"
        f"Price: {selected_dish['price']:.2f} €\n"
        f"Rating: {stars} {rating} / 5\n"
        f"Comment: {comment}"
    )


# RATING-LABEL AKTUALISIEREN

def update_rating_label(value):
    rating = int(round(value))
    stars = rating_to_stars(rating)
    rating_value_label.configure(text=f"{stars} {rating} / 5")


# TAGESANALYSE

def daily_analytics():
    if not file_exists_with_data(ORDERS_FILE):
        show_output("Daily Analytics", "No orders saved yet.")
        return

    orders_count = {}
    selected_day = weekday.get()

    with open(ORDERS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row.get("Dish", "")
            day = row.get("Day", "")

            if day == selected_day and dish != "":
                orders_count[dish] = orders_count.get(dish, 0) + 1

    if not orders_count:
        show_output(
            f"Daily Analytics: {selected_day}",
            "No orders for this day yet."
        )
        return

    text = ""

    for dish, count in orders_count.items():
        text += f"{dish}: {count} orders\n"

    show_output(f"Daily Analytics: {selected_day}", text)


# WOCHENANALYSE

def weekly_analytics():
    orders_count = {}
    rating_sum = {}
    rating_count = {}

    if file_exists_with_data(ORDERS_FILE):
        with open(ORDERS_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row.get("Dish", "")

                if dish != "":
                    orders_count[dish] = orders_count.get(dish, 0) + 1

    if file_exists_with_data(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row.get("Dish", "")
                rating_raw = row.get("Rating", "")

                try:
                    rating = int(rating_raw)
                except ValueError:
                    continue

                if dish != "" and 1 <= rating <= 5:
                    rating_sum[dish] = rating_sum.get(dish, 0) + rating
                    rating_count[dish] = rating_count.get(dish, 0) + 1

    all_dishes = set(orders_count.keys()) | set(rating_sum.keys())

    if not all_dishes:
        show_output("Weekly Analytics", "No orders or ratings saved yet.")
        return

    text = ""

    for dish in sorted(all_dishes):
        orders = orders_count.get(dish, 0)

        if dish in rating_sum:
            average_rating = round(rating_sum[dish] / rating_count[dish], 1)
            stars = rating_to_stars(average_rating)
            rating_text = f"{stars} {average_rating} / 5"
        else:
            rating_text = "No rating yet"

        text += (
            f"{dish}\n"
            f"Orders: {orders}\n"
            f"Average Rating: {rating_text}\n\n"
        )

    show_output("Weekly Analytics", text)


# BELIEBTESTE GERICHTE NACH BEWERTUNG

def popular_dishes_statistics():
    if not file_exists_with_data(FEEDBACK_FILE):
        show_output("Popular Dishes", "No dishes have been rated yet.")
        return

    rating_sum = {}
    rating_count = {}
    latest_feedback = {}

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row.get("Dish", "").strip()
            rating_raw = row.get("Rating", "").strip()
            comment = row.get("Comment", "").strip()

            if dish == "" or rating_raw == "":
                continue

            try:
                rating = int(rating_raw)
            except ValueError:
                continue

            if rating < 1 or rating > 5:
                continue

            rating_sum[dish] = rating_sum.get(dish, 0) + rating
            rating_count[dish] = rating_count.get(dish, 0) + 1
            latest_feedback[dish] = comment

    if not rating_sum:
        show_output("Popular Dishes", "No dishes have been rated yet.")
        return

    ranking = []

    for dish in rating_sum:
        average_rating = round(rating_sum[dish] / rating_count[dish], 1)

        ranking.append({
            "dish": dish,
            "average_rating": average_rating,
            "rating_count": rating_count[dish],
            "latest_feedback": latest_feedback.get(dish, "")
        })

    ranking.sort(
        key=lambda item: (item["average_rating"], item["rating_count"]),
        reverse=True
    )

    text = "Most Popular Dishes by Rating:\n\n"

    for index, item in enumerate(ranking, start=1):
        stars = rating_to_stars(item["average_rating"])

        text += (
            f"{index}. {item['dish']}\n"
            f"Average Rating: {stars} {item['average_rating']} / 5\n"
            f"Number of Ratings: {item['rating_count']}\n"
            f"Latest Feedback: {item['latest_feedback']}\n\n"
        )

    best_dish = ranking[0]
    best_stars = rating_to_stars(best_dish["average_rating"])

    text += (
        f"Best Rated Dish:\n"
        f"{best_dish['dish']} with "
        f"{best_stars} {best_dish['average_rating']} / 5"
    )

    show_output("Popular Dishes", text)


# ALLES ZURÜCKSETZEN

def reset_all_data():
    global user_profile, selected_dish

    confirm = messagebox.askyesno(
        "Reset all data",
        "Do you really want to delete all saved orders, feedback and the saved user profile?"
    )

    if not confirm:
        return

    user_profile = {}
    selected_dish = None

    if os.path.isfile(ORDERS_FILE):
        os.remove(ORDERS_FILE)

    if os.path.isfile(FEEDBACK_FILE):
        os.remove(FEEDBACK_FILE)

    if os.path.isfile(PROFILE_FILE):
        os.remove(PROFILE_FILE)

    comment_box.delete("1.0", "end")

    slider.set(3)
    update_rating_label(3)

    show_output(
        "Reset completed",
        "All data has been reset successfully.\n\n"
        "Deleted:\n"
        "- Orders\n"
        "- Feedback\n"
        "- Saved user profile\n\n"
        "You can now start again from zero."
    )


# HAUPTFENSTER

root = ctk.CTk()
root.configure(fg_color=APP_BG)
root.geometry("1000x700")
root.title("NutriWork")


# OBERER BEREICH

top_frame = ctk.CTkFrame(
    root,
    fg_color=APP_BG
)
top_frame.pack(fill="x", padx=20, pady=(20, 10))


# TITEL MITTIG

title_label = ctk.CTkLabel(
    top_frame,
    text="NutriWork Dashboard",
    font=("Arial", 30, "bold"),
    text_color=TEXT_COLOR
)
title_label.pack(pady=(0, 12))


# BUTTONS MITTIG UNTER DER ÜBERSCHRIFT

top_buttons_frame = ctk.CTkFrame(
    top_frame,
    fg_color=APP_BG
)
top_buttons_frame.pack(anchor="center")

profile_button = ctk.CTkButton(
    top_buttons_frame,
    text="Create User Profile",
    command=open_profile_window,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
profile_button.pack(side="left", padx=8)

daily_button = ctk.CTkButton(
    top_buttons_frame,
    text="Daily analytics",
    command=daily_analytics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
daily_button.pack(side="left", padx=8)

weekly_button = ctk.CTkButton(
    top_buttons_frame,
    text="Weekly analytics",
    command=weekly_analytics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
weekly_button.pack(side="left", padx=8)

popular_button = ctk.CTkButton(
    top_buttons_frame,
    text="Popular dishes",
    command=popular_dishes_statistics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
popular_button.pack(side="left", padx=8)

reset_button = ctk.CTkButton(
    top_buttons_frame,
    text="Reset all data",
    command=reset_all_data,
    fg_color=RESET_COLOR,
    hover_color=RESET_HOVER,
    text_color="black"
)
reset_button.pack(side="left", padx=8)


# MAIN FRAME

main_frame = ctk.CTkFrame(root, fg_color=APP_BG)
main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


# LINKE SEITE

left_frame = ctk.CTkFrame(
    main_frame,
    fg_color=CARD_BG,
    corner_radius=15
)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

dish_title = ctk.CTkLabel(
    left_frame,
    text="Choose the day",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
dish_title.pack(pady=10)

weekday = ctk.CTkOptionMenu(
    left_frame,
    values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    command=new_dishes
)
weekday.pack(pady=(0, 20))


# GERICHTE

dishes_label = ctk.CTkLabel(
    left_frame,
    text="Today's Dishes",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
dishes_label.pack(pady=(10, 5))

dishes_frame = ctk.CTkFrame(
    left_frame,
    fg_color=CARD_BG
)
dishes_frame.pack(fill="x")


# RECHTE SEITE

right_frame = ctk.CTkFrame(
    main_frame,
    fg_color=CARD_BG,
    corner_radius=15
)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

details_title = ctk.CTkLabel(
    right_frame,
    text="Dish Details",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
details_title.pack(pady=10)

details_textbox = ctk.CTkTextbox(
    right_frame,
    width=430,
    height=280,
    font=("Arial", 16)
)
details_textbox.pack(pady=10)
details_textbox.insert("1.0", "Select a dish")
details_textbox.configure(state="disabled")


# BESTELLBUTTON

order_button = ctk.CTkButton(
    right_frame,
    text="Order",
    command=order_dish,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
order_button.pack(padx=30, pady=10)


# FEEDBACK-BEREICH

feedback_label = ctk.CTkLabel(
    right_frame,
    text="Rate this dish from 1 to 5:",
    font=("Arial", 18),
    text_color=TEXT_COLOR
)
feedback_label.pack(pady=(10, 5))

rating_value_label = ctk.CTkLabel(
    right_frame,
    text="★★★☆☆ 3 / 5",
    font=("Arial", 16),
    text_color=TEXT_COLOR
)
rating_value_label.pack(pady=(0, 5))

slider = ctk.CTkSlider(
    right_frame,
    from_=1,
    to=5,
    number_of_steps=4,
    command=update_rating_label
)
slider.set(3)
slider.pack(pady=10)

comment_box = ctk.CTkTextbox(
    right_frame,
    width=310,
    height=100
)
comment_box.pack(pady=10)

submit_button = ctk.CTkButton(
    right_frame,
    text="Submit Feedback",
    command=save_feedback,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
submit_button.pack(padx=5, pady=5)


# START

load_user_profile_from_file()
new_dishes()
root.mainloop()# GERICHTE DES WOCHENPLANS


schedule = {
    "Monday": [
        {
            "name": "Chicken Bowl",
            "kcal": 650,
            "protein": 42,
            "carbs": 51,
            "fat": 14,
            "allergens": "Gluten, Soy, Sesame",
            "score": "8.4 / 10"
        },
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish",
            "score": "8.2 / 10"
        }
    ],

    "Tuesday": [
        {
            "name": "Pasta Napoli",
            "kcal": 610,
            "protein": 20,
            "carbs": 108,
            "fat": 11,
            "allergens": "Gluten, Milk",
            "score": "7.5 / 10"
        },
        {
            "name": "Chicken Bowl",
            "kcal": 650,
            "protein": 42,
            "carbs": 51,
            "fat": 14,
            "allergens": "Gluten, Soy, Sesame",
            "score": "8.4 / 10"
        }
    ],

    "Wednesday": [
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish",
            "score": "8.2 / 10"
        }
    ],

    "Thursday": [
        {
            "name": "Pasta Napoli",
            "kcal": 610,
            "protein": 20,
            "carbs": 108,
            "fat": 11,
            "allergens": "Gluten, Milk",
            "score": "7.5 / 10"
        }
    ],

    "Friday": [
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish",
            "score": "8.2 / 10"
        }
    ]
}


# HILFSFUNKTIONEN

def show_output(title, text):
    details_title.configure(text=title)

    details_textbox.configure(state="normal")
    details_textbox.delete("1.0", "end")
    details_textbox.insert("1.0", text)
    details_textbox.configure(state="disabled")


def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ensure_csv_file(file_path, header):
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)


def file_exists_with_data(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) > 0


def rating_to_stars(rating):
    full_stars = int(round(rating))
    empty_stars = 5 - full_stars
    return "★" * full_stars + "☆" * empty_stars


def create_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER,
        text_color="black"
    )


# USER PROFILE


def open_profile_window():
    new_window = ctk.CTkToplevel(root)
    new_window.title("User Profile")
    new_window.geometry("400x430")
    new_window.grab_set()

    gender_label = ctk.CTkLabel(
        new_window,
        text="Gender",
        font=("Arial", 18)
    )
    gender_label.pack(pady=(20, 5))

    gender = ctk.CTkOptionMenu(
        new_window,
        values=["Male", "Female", "Diver"]
    )
    gender.pack()

    weight_label = ctk.CTkLabel(
        new_window,
        text="Weight in kg",
        font=("Arial", 18)
    )
    weight_label.pack(pady=(20, 5))

    weight_entry = ctk.CTkEntry(
        new_window,
        placeholder_text="e.g. 70"
    )
    weight_entry.pack()

    goal_label = ctk.CTkLabel(
        new_window,
        text="Goal",
        font=("Arial", 18)
    )
    goal_label.pack(pady=(20, 5))

    goal_option = ctk.CTkOptionMenu(
        new_window,
        values=["Build Muscle", "Lose Weight", "Maintain Weight"]
    )
    goal_option.pack()

    def save_profile():
        global user_profile

        weight = weight_entry.get().strip()

        if weight == "":
            show_output("User Profile", "Please enter your weight.")
            return

        try:
            float(weight)
        except ValueError:
            show_output("User Profile", "Please enter a valid weight.")
            return

        user_profile = {
            "gender": gender.get(),
            "weight": weight,
            "goal": goal_option.get()
        }

        show_output(
            "User Profile",
            f"Profile saved successfully!\n\n"
            f"Gender: {user_profile['gender']}\n"
            f"Weight: {user_profile['weight']} kg\n"
            f"Goal: {user_profile['goal']}"
        )

        new_window.destroy()

    save_button = create_button(
        new_window,
        "Save Profile",
        save_profile
    )
    save_button.pack(pady=25)

# GERICHTE


def new_dishes(day=None):
    for widget in dishes_frame.winfo_children():
        widget.destroy()

    chosen_day = weekday.get()

    for dish in schedule[chosen_day]:
        button = ctk.CTkButton(
            dishes_frame,
            text=dish["name"],
            height=50,
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER,
            text_color="black",
            command=lambda d=dish: show_dish(d)
        )
        button.pack(fill="x", padx=20, pady=10)


def show_dish(dish):
    global selected_dish
    selected_dish = dish

    text = (
        f"Name: {dish['name']}\n\n"
        f"Calories: {dish['kcal']} kcal\n"
        f"Protein: {dish['protein']} g\n"
        f"Carbs: {dish['carbs']} g\n"
        f"Fat: {dish['fat']} g\n\n"
        f"Allergens: {dish['allergens']}\n\n"
        f"Health Score: {dish['score']}"
    )

    if user_profile.get("goal") == "Build Muscle":
        try:
            weight = float(user_profile["weight"])
            protein_goal = weight * 2
            protein_percent = round(dish["protein"] / protein_goal * 100)
            if protein_percent >= 25:
                text +=(
                    f"\n\nProtein Coverage: {protein_percent}%"
                    f"\nRecommended for muscle gain."
                    )
            else:
                text += (f"\n\nProtein Coverage: {protein_percent}%")

        except ValueError:
            text += "\n\nPlease enter a valid weight in your profile."

    show_output("Dish Details", text)


# BESTELLUNG SPEICHERN


def order_dish():
    if selected_dish is None:
        show_output("Order", "Please select a dish first.")
        return

    ensure_csv_file(
        ORDERS_FILE,
        ["Date", "Dish", "Amount", "Day"]
    )

    with open(ORDERS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            get_current_datetime(),
            selected_dish["name"],
            1,
            weekday.get()
        ])

    show_output(
        "Order",
        f"Order saved successfully!\n\n"
        f"Dish: {selected_dish['name']}\n"
        f"Day: {weekday.get()}"
    )


# FEEDBACK SPEICHERN

def save_feedback():
    if selected_dish is None:
        show_output("Feedback", "Please select a dish first.")
        return

    rating = int(round(slider.get()))
    comment = comment_box.get("1.0", "end").strip()

    if comment == "":
        show_output("Feedback", "Please enter a feedback comment.")
        return

    ensure_csv_file(
        FEEDBACK_FILE,
        ["Date", "Dish", "Rating", "Comment"]
    )

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            get_current_datetime(),
            selected_dish["name"],
            rating,
            comment
        ])

    comment_box.delete("1.0", "end")

    stars = rating_to_stars(rating)

    show_output(
        "Feedback",
        f"Feedback saved successfully!\n\n"
        f"Dish: {selected_dish['name']}\n"
        f"Rating: {stars} {rating} / 5\n"
        f"Comment: {comment}"
    )


# RATING-LABEL AKTUALISIEREN

def update_rating_label(value):
    rating = int(round(value))
    stars = rating_to_stars(rating)
    rating_value_label.configure(text=f"{stars} {rating} / 5")


# TAGESANALYSE


def daily_analytics():
    if not file_exists_with_data(ORDERS_FILE):
        show_output("Daily Analytics", "No orders saved yet.")
        return

    orders_count = {}
    selected_day = weekday.get()

    with open(ORDERS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row.get("Dish", "")
            day = row.get("Day", "")

            if day == selected_day and dish != "":
                orders_count[dish] = orders_count.get(dish, 0) + 1

    if not orders_count:
        show_output(
            f"Daily Analytics: {selected_day}",
            "No orders for this day yet."
        )
        return

    text = ""

    for dish, count in orders_count.items():
        text += f"{dish}: {count} orders\n"

    show_output(f"Daily Analytics: {selected_day}", text)


# WOCHENANALYSE


def weekly_analytics():
    orders_count = {}
    rating_sum = {}
    rating_count = {}

    if file_exists_with_data(ORDERS_FILE):
        with open(ORDERS_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row.get("Dish", "")

                if dish != "":
                    orders_count[dish] = orders_count.get(dish, 0) + 1

    if file_exists_with_data(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row.get("Dish", "")
                rating_raw = row.get("Rating", "")

                try:
                    rating = int(rating_raw)
                except ValueError:
                    continue

                if dish != "" and 1 <= rating <= 5:
                    rating_sum[dish] = rating_sum.get(dish, 0) + rating
                    rating_count[dish] = rating_count.get(dish, 0) + 1

    all_dishes = set(orders_count.keys()) | set(rating_sum.keys())

    if not all_dishes:
        show_output("Weekly Analytics", "No orders or ratings saved yet.")
        return

    text = ""

    for dish in sorted(all_dishes):
        orders = orders_count.get(dish, 0)

        if dish in rating_sum:
            average_rating = round(rating_sum[dish] / rating_count[dish], 1)
            stars = rating_to_stars(average_rating)
            rating_text = f"{stars} {average_rating} / 5"
        else:
            rating_text = "No rating yet"

        text += (
            f"{dish}\n"
            f"Orders: {orders}\n"
            f"Average Rating: {rating_text}\n\n"
        )

    show_output("Weekly Analytics", text)


# BELIEBTESTE GERICHTE NACH BEWERTUNG

def popular_dishes_statistics():
    if not file_exists_with_data(FEEDBACK_FILE):
        show_output("Popular Dishes", "No dishes have been rated yet.")
        return

    rating_sum = {}
    rating_count = {}
    latest_feedback = {}

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row.get("Dish", "").strip()
            rating_raw = row.get("Rating", "").strip()
            comment = row.get("Comment", "").strip()

            if dish == "" or rating_raw == "":
                continue

            try:
                rating = int(rating_raw)
            except ValueError:
                continue

            if rating < 1 or rating > 5:
                continue

            rating_sum[dish] = rating_sum.get(dish, 0) + rating
            rating_count[dish] = rating_count.get(dish, 0) + 1
            latest_feedback[dish] = comment

    if not rating_sum:
        show_output("Popular Dishes", "No dishes have been rated yet.")
        return

    ranking = []

    for dish in rating_sum:
        average_rating = round(rating_sum[dish] / rating_count[dish], 1)

        ranking.append({
            "dish": dish,
            "average_rating": average_rating,
            "rating_count": rating_count[dish],
            "latest_feedback": latest_feedback.get(dish, "")
        })

    ranking.sort(
        key=lambda item: (item["average_rating"], item["rating_count"]),
        reverse=True
    )

    text = "Most Popular Dishes by Rating:\n\n"

    for index, item in enumerate(ranking, start=1):
        stars = rating_to_stars(item["average_rating"])

        text += (
            f"{index}. {item['dish']}\n"
            f"Average Rating: {stars} {item['average_rating']} / 5\n"
            f"Number of Ratings: {item['rating_count']}\n"
            f"Latest Feedback: {item['latest_feedback']}\n\n"
        )

    best_dish = ranking[0]
    best_stars = rating_to_stars(best_dish["average_rating"])

    text += (
        f"Best Rated Dish:\n"
        f"{best_dish['dish']} with "
        f"{best_stars} {best_dish['average_rating']} / 5"
    )

    show_output("Popular Dishes", text)


# ALLES ZURÜCKSETZEN


def reset_all_data():
    global user_profile, selected_dish

    confirm = messagebox.askyesno(
        "Reset all data",
        "Do you really want to delete all saved orders, feedback and the current user profile?"
    )

    if not confirm:
        return

    user_profile = {}
    selected_dish = None

    if os.path.isfile(ORDERS_FILE):
        os.remove(ORDERS_FILE)

    if os.path.isfile(FEEDBACK_FILE):
        os.remove(FEEDBACK_FILE)

    comment_box.delete("1.0", "end")

    slider.set(3)
    update_rating_label(3)

    show_output(
        "Reset completed",
        "All data has been reset successfully.\n\n"
        "Deleted:\n"
        "- Orders\n"
        "- Feedback\n"
        "- Current user profile\n\n"
        "You can now start again from zero."
    )


# HAUPTFENSTER


root = ctk.CTk()
root.configure(fg_color=APP_BG)
root.geometry("1000x700")
root.title("NutriWork")


# OBERER BEREICH

top_frame = ctk.CTkFrame(
    root,
    fg_color=APP_BG
)
top_frame.pack(fill="x", padx=20, pady=(20, 10))


# TITEL MITTIG

title_label = ctk.CTkLabel(
    top_frame,
    text="NutriWork Dashboard",
    font=("Arial", 30, "bold"),
    text_color=TEXT_COLOR
)
title_label.pack(pady=(0, 12))


# BUTTONS MITTIG UNTER DER ÜBERSCHRIFT

top_buttons_frame = ctk.CTkFrame(
    top_frame,
    fg_color=APP_BG
)
top_buttons_frame.pack(anchor="center")

profile_button = ctk.CTkButton(
    top_buttons_frame,
    text="Create User Profile",
    command=open_profile_window,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
profile_button.pack(side="left", padx=8)

daily_button = ctk.CTkButton(
    top_buttons_frame,
    text="Daily analytics",
    command=daily_analytics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
daily_button.pack(side="left",padx=8)

weekly_button = ctk.CTkButton(
    top_buttons_frame,
    text="Weekly analytics",
    command=weekly_analytics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
weekly_button.pack(side="left",padx=8)

popular_button = ctk.CTkButton(
    top_buttons_frame,
    text="Popular dishes",
    command=popular_dishes_statistics,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
popular_button.pack(side="left",padx=8)




reset_button = ctk.CTkButton(
    top_buttons_frame,
    text="Reset all data",
    command=reset_all_data,
    fg_color=RESET_COLOR,
    hover_color=RESET_HOVER,
    text_color="black"
)
reset_button.pack(side="left", padx=8)


# MAIN FRAME

main_frame = ctk.CTkFrame(root, fg_color=APP_BG)
main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


# LINKE SEITE

left_frame = ctk.CTkFrame(
    main_frame,
    fg_color=CARD_BG,
    corner_radius=15
)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

dish_title = ctk.CTkLabel(
    left_frame,
    text="Choose the day",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
dish_title.pack(pady=10)

weekday = ctk.CTkOptionMenu(
    left_frame,
    values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    command=new_dishes
)
weekday.pack(pady=(0, 20))


# GERICHTE

dishes_label = ctk.CTkLabel(
    left_frame,
    text="Today's Dishes",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
dishes_label.pack(pady=(10, 5))

dishes_frame = ctk.CTkFrame(
    left_frame,
    fg_color=CARD_BG
)
dishes_frame.pack(fill="x")


# RECHTE SEITE

right_frame = ctk.CTkFrame(
    main_frame,
    fg_color=CARD_BG,
    corner_radius=15
)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

details_title = ctk.CTkLabel(
    right_frame,
    text="Dish Details",
    font=("Arial", 22, "bold"),
    text_color=TEXT_COLOR
)
details_title.pack(pady=10)

details_textbox = ctk.CTkTextbox(
    right_frame,
    width=430,
    height=280,
    font=("Arial", 16)
)
details_textbox.pack(pady=10)
details_textbox.insert("1.0", "Select a dish")
details_textbox.configure(state="disabled")


# BESTELLBUTTON

order_button = ctk.CTkButton(
    right_frame,
    text="Order",
    command=order_dish,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
order_button.pack(padx=30, pady=10)

# FEEDBACK-BEREICH

feedback_label = ctk.CTkLabel(
    right_frame,
    text="Rate this dish from 1 to 5:",
    font=("Arial", 18),
    text_color=TEXT_COLOR
)
feedback_label.pack(pady=(10, 5))

rating_value_label = ctk.CTkLabel(
    right_frame,
    text="★★★☆☆ 3 / 5",
    font=("Arial", 16),
    text_color=TEXT_COLOR
)
rating_value_label.pack(pady=(0, 5))

slider = ctk.CTkSlider(
    right_frame,
    from_=1,
    to=5,
    number_of_steps=4,
    command=update_rating_label
)
slider.set(3)
slider.pack(pady=10)

comment_box = ctk.CTkTextbox(
    right_frame,
    width=310,
    height=100
)
comment_box.pack(pady=10)

submit_button = ctk.CTkButton(
    right_frame,
    text="Submit Feedback",
    command=save_feedback,
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="black"
)
submit_button.pack(padx=5, pady=5)

# START

new_dishes()
root.mainloop()
