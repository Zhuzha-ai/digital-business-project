import customtkinter as ctk
import csv
import os


# SETTINGS

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# HAUPTFENSTER

root = ctk.CTk()
root.configure(fg_color="#F3F5F0")
root.geometry("1000x700")
root.title("NutriWork")


# TITEL

title_label = ctk.CTkLabel(
    root,
    text="NutriWork Dashboard",
    font=("Arial", 30, "bold"),
    text_color="#2B2B2B"
)
title_label.pack(pady=(20, 10))


# GLOBALE VARIABLEN

user_profile = {}
selected_dish = None


# GERICHTE DES WOCHENPLANS

schedule = {
    "Monday": [
        {
            "name": "Chicken Bowl",
            "kcal": 650,
            "protein": 42,
            "carbs": 51,
            "fat": 14,
            "allergens": "Gluten, Soy, Sesame"
        },
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish"
        }
    ],

    "Tuesday": [
        {
            "name": "Pasta Napoli",
            "kcal": 610,
            "protein": 20,
            "carbs": 108,
            "fat": 11,
            "allergens": "Gluten, Milk"
        },
        {
            "name": "Chicken Bowl",
            "kcal": 650,
            "protein": 42,
            "carbs": 51,
            "fat": 14,
            "allergens": "Gluten, Soy, Sesame"
        }
    ],

    "Wednesday": [
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish"
        }
    ],

    "Thursday": [
        {
            "name": "Pasta Napoli",
            "kcal": 610,
            "protein": 20,
            "carbs": 108,
            "fat": 11,
            "allergens": "Gluten, Milk"
        }
    ],

    "Friday": [
        {
            "name": "Salmon Rice",
            "kcal": 700,
            "protein": 44,
            "carbs": 72,
            "fat": 28,
            "allergens": "Fish"
        }
    ]
}


# FUNKTION ZUM ÖFFNEN DES PROFILFENSTERS

def open_profile_window():
    new_window = ctk.CTkToplevel(root)
    new_window.title("User Profile")
    new_window.geometry("400x400")
    new_window.grab_set()

    gender_label = ctk.CTkLabel(
        new_window,
        text="Gender",
        font=("Arial", 18)
    )
    gender_label.pack()

    gender = ctk.CTkOptionMenu(
        new_window,
        values=["Male", "Female", "Diver"]
    )
    gender.pack()

    weight_label = ctk.CTkLabel(
        new_window,
        text="Weight",
        font=("Arial", 18)
    )
    weight_label.pack()

    weight_entry = ctk.CTkEntry(new_window)
    weight_entry.pack()

    goal_label = ctk.CTkLabel(
        new_window,
        text="Goal",
        font=("Arial", 18)
    )
    goal_label.pack()

    goal_option = ctk.CTkOptionMenu(
        new_window,
        values=[
            "Build Muscle",
            "Lose Weight",
            "Maintain Weight"
        ]
    )
    goal_option.pack()

    def save_profile():
        global user_profile

        user_profile = {
            "gender": gender.get(),
            "weight": weight_entry.get(),
            "goal": goal_option.get()
        }

        details_label.configure(text="Profile saved successfully!")
        new_window.destroy()

    save_button = ctk.CTkButton(
        new_window,
        text="Save",
        command=save_profile
    )
    save_button.pack(pady=20)


# PROFIL-BUTTON

profile_button = ctk.CTkButton(
    root,
    text="Create User Profile",
    command=open_profile_window,
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black"
)
profile_button.pack(pady=(0, 10))


# MAIN FRAME

main_frame = ctk.CTkFrame(root, fg_color="#F3F5F0")
main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


# LINKE SEITE

left_frame = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=15)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

dish_title = ctk.CTkLabel(
    left_frame,
    text="Choose the day",
    font=("Arial", 22, "bold")
)
dish_title.pack(pady=10)

dishes_frame = ctk.CTkFrame(left_frame, fg_color="white")

dishes_label = ctk.CTkLabel(
    left_frame,
    text="Today's Dishes",
    font=("Arial", 22, "bold")
)


# GERICHTE FÜR DEN AUSGEWÄHLTEN TAG AKTUALISIEREN

def new_dishes(day):
    for widget in dishes_frame.winfo_children():
        widget.destroy()

    chosen_day = weekday.get()

    for dish in schedule[chosen_day]:
        button = ctk.CTkButton(
            dishes_frame,
            text=dish["name"],
            height=50,
            fg_color="#A8C3A0",
            hover_color="#8FAE87",
            text_color="black",
            command=lambda d=dish: show_dish(d)
        )
        button.pack(fill="x", padx=20, pady=10)


# TAGESANALYSE

def daily_analytics():
    orders_count = {}

    if not os.path.isfile("orders.csv"):
        details_title.configure(text="Daily Analytics")
        details_label.configure(text="No orders saved yet.")
        return

    with open("orders.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        day = weekday.get()

        for row in reader:
            dish = row["Dish"]

            if row["Day"] == day:
                orders_count[dish] = orders_count.get(dish, 0) + 1

    if not orders_count:
        details_title.configure(text=f"Daily Analytics: {weekday.get()}")
        details_label.configure(text="No orders for this day yet.")
        return

    text_l = ""

    for dish, count in orders_count.items():
        text_l += f"{dish}: {count}\n"

    details_title.configure(text=f"Daily Analytics: {weekday.get()}")
    details_label.configure(text=text_l)


# WOCHENANALYSE

def weekly_analytics():
    orders_count = {}
    rating_sum = {}
    rating_count = {}

    if not os.path.isfile("orders.csv"):
        details_title.configure(text="Weekly Analytics")
        details_label.configure(text="No orders saved yet.")
        return

    with open("orders.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row["Dish"]
            orders_count[dish] = orders_count.get(dish, 0) + 1

    if os.path.isfile("feedback.csv"):
        with open("feedback.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish = row["Dish"]
                rating = int(row["Rating"])

                rating_sum[dish] = rating_sum.get(dish, 0) + rating
                rating_count[dish] = rating_count.get(dish, 0) + 1

    text_l = ""

    for dish, count in orders_count.items():
        if dish in rating_sum:
            avg_rating = round(rating_sum[dish] / rating_count[dish], 1)
        else:
            avg_rating = "No rating yet"

        text_l += f"{dish}\nOrders: {count}\nRating: {avg_rating}\n\n"

    details_title.configure(text="Weekly Analytics")
    details_label.configure(text=text_l)


# BELIEBTESTE GERICHTE STATISTIK

def popular_dishes_statistics():
    orders_count = {}

    if not os.path.isfile("orders.csv"):
        details_title.configure(text="Popular Dishes")
        details_label.configure(text="No orders saved yet.")
        return

    with open("orders.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dish = row["Dish"]
            orders_count[dish] = orders_count.get(dish, 0) + 1

    if not orders_count:
        details_title.configure(text="Popular Dishes")
        details_label.configure(text="No orders saved yet.")
        return

    sorted_dishes = sorted(
        orders_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    text_l = "Most Popular Dishes:\n\n"

    for place, (dish, count) in enumerate(sorted_dishes, start=1):
        text_l += f"{place}. {dish}: {count} orders\n"

    most_popular_dish = sorted_dishes[0][0]
    most_popular_count = sorted_dishes[0][1]

    text_l += (
        f"\n🏆 Most popular dish:\n"
        f"{most_popular_dish} with {most_popular_count} orders"
    )

    details_title.configure(text="Popular Dishes")
    details_label.configure(text=text_l)


# WOCHENTAGS-AUSWAHL

weekday = ctk.CTkOptionMenu(
    left_frame,
    values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    command=new_dishes
)
weekday.pack(pady=(0, 20))


# ANALYSE-BUTTONS

daily_analytics_button = ctk.CTkButton(
    left_frame,
    text="Daily analytics",
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black",
    command=daily_analytics
)

weekly_analytics_button = ctk.CTkButton(
    left_frame,
    text="Weekly analytics",
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black",
    command=weekly_analytics
)

popular_dishes_button = ctk.CTkButton(
    left_frame,
    text="Popular dishes",
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black",
    command=popular_dishes_statistics
)

daily_analytics_button.pack(pady=(0, 20))
weekly_analytics_button.pack(pady=(0, 20))
popular_dishes_button.pack(pady=(0, 20))

dishes_label.pack(pady=(10, 5))
dishes_frame.pack(fill="x")


# RECHTE SEITE

right_frame = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=15)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

details_title = ctk.CTkLabel(
    right_frame,
    text="Dish Details",
    font=("Arial", 22, "bold")
)
details_title.pack(pady=10)

details_label = ctk.CTkLabel(
    right_frame,
    text="Select a dish",
    font=("Arial", 18)
)
details_label.pack(pady=20)


# DETAILS DES AUSGEWÄHLTEN GERICHTS ANZEIGEN

def show_dish(dish):
    global selected_dish
    selected_dish = dish

    details_title.configure(text="Dish Details")

    if dish["name"] == "Chicken Bowl":
        text = f"""
Name: {dish["name"]}

Calories: {dish["kcal"]} kcal

Protein: {dish["protein"]} g

Carbs: {dish["carbs"]} g

Fat: {dish["fat"]} g

Allergens: {dish["allergens"]}

🟢 Health Score: 8,4 / 10
"""

    elif dish["name"] == "Pasta Napoli":
        text = f"""
Name: {dish["name"]}

Calories: {dish["kcal"]} kcal

Protein: {dish["protein"]} g

Carbs: {dish["carbs"]} g

Fat: {dish["fat"]} g

Allergens: {dish["allergens"]}

🟡 Health Score: 7,5 / 10
"""

    elif dish["name"] == "Salmon Rice":
        text = f"""
Name: {dish["name"]}

Calories: {dish["kcal"]} kcal

Protein: {dish["protein"]} g

Carbs: {dish["carbs"]} g

Fat: {dish["fat"]} g

Allergens: {dish["allergens"]}

🟢 Health Score: 8,2 / 10
"""

    else:
        text = "No details available."

    if "goal" in user_profile and user_profile.get("weight"):
        try:
            protein_percent = round(
                dish["protein"] / (float(user_profile["weight"]) * 2) * 100
            )

            if user_profile["goal"] == "Build Muscle":
                text += (
                    f"\nProtein Coverage: {protein_percent}%"
                    f"\n✔ Recommended for muscle gain"
                )

        except ValueError:
            text += "\nPlease enter a valid weight in your profile."

    details_label.configure(text=text)


# BESTELLUNG SPEICHERN

def order_dish():
    if selected_dish is None:
        details_label.configure(text="Please select a dish first.")
        return

    amount = 1
    day = weekday.get()

    order_file = os.path.isfile("orders.csv")

    with open("orders.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not order_file:
            writer.writerow(["Dish", "Amount", "Day"])

        writer.writerow([
            selected_dish["name"],
            amount,
            day
        ])

    details_label.configure(text="Order saved successfully!")


# FEEDBACK SPEICHERN

def save_feedback():
    if selected_dish is None:
        details_label.configure(text="Please select a dish first.")
        return

    rating = int(slider.get())
    comment = comment_box.get("1.0", "end").strip()

    file_exists = os.path.isfile("feedback.csv")

    with open("feedback.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Dish", "Rating", "Comment"])

        writer.writerow([
            selected_dish["name"],
            rating,
            comment
        ])

    comment_box.delete("1.0", "end")
    details_label.configure(text="Feedback saved successfully!")


# BESTELLBUTTON

order_button = ctk.CTkButton(
    right_frame,
    text="Order",
    command=order_dish,
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black"
)
order_button.pack(padx=30, pady=10)


# FEEDBACK-BEREICH

feedback_label = ctk.CTkLabel(
    right_frame,
    text="Rate this dish:",
    font=("Arial", 18)
)
feedback_label.pack(pady=10)

slider = ctk.CTkSlider(
    right_frame,
    from_=1,
    to=5,
    number_of_steps=4
)
slider.pack(pady=10)

comment_box = ctk.CTkTextbox(
    right_frame,
    width=300,
    height=120
)
comment_box.pack(pady=10)

submit_button = ctk.CTkButton(
    right_frame,
    text="Submit Feedback",
    command=save_feedback,
    fg_color="#A8C3A0",
    hover_color="#8FAE87",
    text_color="black"
)
submit_button.pack(padx=5, pady=5)


# GERICHTE BEIM START LADEN

new_dishes(None)


# APP STARTEN

root.mainloop()
