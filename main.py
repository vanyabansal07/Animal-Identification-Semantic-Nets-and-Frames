
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# --------------------------------
# 1. SEMANTIC NETWORK
# --------------------------------

IS_A = {
    "Lion": "Mammal",
    "Tiger": "Mammal",
    "Elephant": "Mammal",
    "Shark": "Fish",
    "Eagle": "Bird"
}

# --------------------------------
# 2. FRAMES - ANIMAL PROPERTIES
# --------------------------------

ANIMALS = {
    "Lion": {
        "habitat": "Grassland",
        "food": "Meat",
        "legs": 4,
        "covering": "Fur"
    },

    "Tiger": {
        "habitat": "Forest",
        "food": "Meat",
        "legs": 4,
        "covering": "Fur"
    },

    "Elephant": {
        "habitat": "Land",
        "food": "Plants",
        "legs": 4,
        "covering": "Skin"
    },

    "Shark": {
        "habitat": "Water",
        "food": "Meat",
        "legs": 0,
        "covering": "Scales"
    },

    "Eagle": {
        "habitat": "Air",
        "food": "Meat",
        "legs": 2,
        "covering": "Feathers"
    }
}

ANIMAL_INFO = {
    "Lion": "The lion is a wild mammal known as the King of the Jungle.",
    "Tiger": "The tiger is a large wild cat with black stripes.",
    "Elephant": "The elephant is a large land mammal with a trunk.",
    "Shark": "The shark is an aquatic fish with a cartilaginous skeleton.",
    "Eagle": "The eagle is a bird known for its strong vision."
}

# --------------------------------
# 3. IDENTIFICATION FUNCTION
# --------------------------------

def identify_animal():

    habitat = habitat_box.get()
    food = food_box.get()
    legs = legs_box.get()
    covering = covering_box.get()

    if not all([habitat, food, legs, covering]):
        messagebox.showwarning(
            "Missing Information",
            "Please select all animal features."
        )
        return

    legs = int(legs)

    best_score = 0
    best_animals = []

    for animal, features in ANIMALS.items():

        score = 0

        if features["habitat"] == habitat:
            score += 1

        if features["food"] == food:
            score += 1

        if features["legs"] == legs:
            score += 1

        if features["covering"] == covering:
            score += 1

        if score > best_score:
            best_score = score
            best_animals = [animal]

        elif score == best_score:
            best_animals.append(animal)

    if best_score >= 3:

        animal = best_animals[0]

        image_label.config(image=animal_images[animal])
        image_label.image = animal_images[animal]

        result_label.config(
            text=(
                "Identified Animal: " + animal +
                "\nCategory: " + IS_A[animal] +
                "\nMatching Features: " + str(best_score) + "/4" +
                "\n\nCharacteristics:\n" + ANIMAL_INFO[animal]
            ),
            fg="#087443"
        )

    else:
        result_label.config(
            text="Animal could not be identified confidently.\n"
            "Please try different features.",
            fg="#b42318"
        )

# --------------------------------
# 4. RESET FUNCTION
# --------------------------------

def reset_fields():

    habitat_box.set("")
    food_box.set("")
    legs_box.set("")
    covering_box.set("")

    result_label.config(
        text="Select features to identify an animal.",
        fg="#333333"
    )

    image_label.config(image="")
    image_label.image = None

# --------------------------------
# 5. GUI WINDOW
# --------------------------------

root = tk.Tk()

root.title("Animal Identification System")
root.geometry("700x750")
root.configure(bg="#eef5f2")
root.resizable(True, True)

# --------------------------------
# 6. LOAD ANIMAL IMAGES
# --------------------------------

animal_images = {}

for animal in ["Lion", "Tiger", "Elephant", "Shark", "Eagle"]:

    img = Image.open("images/" + animal.lower() + ".png")
    img = img.resize((180, 130))

    animal_images[animal] = ImageTk.PhotoImage(img, master=root)

# --------------------------------
# 7. TITLE AND SUBTITLE
# --------------------------------

title = tk.Label(
    root,
    text="ANIMAL IDENTIFICATION SYSTEM",
    font=("Arial", 19, "bold"),
    bg="#eef5f2",
    fg="#155e45"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Using Semantic Networks and Frames",
    font=("Arial", 11),
    bg="#eef5f2"
)
subtitle.pack(pady=5)

# --------------------------------
# 8. INPUT FRAME
# --------------------------------

frame = tk.Frame(
    root,
    bg="white",
    padx=30,
    pady=20
)
frame.pack(pady=15)

# --------------------------------
# 9. DROPDOWN FUNCTION
# --------------------------------

def add_dropdown(label, values, row):

    tk.Label(
        frame,
        text=label,
        font=("Arial", 11, "bold"),
        bg="white"
    ).grid(row=row, column=0, padx=10, pady=12, sticky="w")

    box = ttk.Combobox(
        frame,
        values=values,
        state="readonly",
        width=22,
        font=("Arial", 10)
    )

    box.grid(row=row, column=1, padx=10, pady=12)

    return box

# --------------------------------
# 10. INPUT DROPDOWNS
# --------------------------------

habitat_box = add_dropdown(
    "Select Habitat:",
    ["Grassland", "Forest", "Land", "Water", "Air"],
    0
)

food_box = add_dropdown(
    "Select Food:",
    ["Meat", "Plants"],
    1
)

legs_box = add_dropdown(
    "Number of Legs:",
    ["0", "2", "4"],
    2
)

covering_box = add_dropdown(
    "Body Covering:",
    ["Fur", "Skin", "Scales", "Feathers"],
    3
)

# --------------------------------
# 11. IDENTIFY BUTTON
# --------------------------------

identify_button = tk.Button(
    root,
    text="IDENTIFY ANIMAL",
    font=("Arial", 12, "bold"),
    width=22,
    bg="#18794e",
    fg="white",
    command=identify_animal
)
identify_button.pack(pady=12)

# --------------------------------
# 12. RESET BUTTON
# --------------------------------

reset_button = tk.Button(
    root,
    text="RESET",
    font=("Arial", 10),
    width=15,
    command=reset_fields
)
reset_button.pack(pady=5)

# --------------------------------
# 13. RESULT LABEL
# --------------------------------

result_label = tk.Label(
    root,
    text="Select features to identify an animal.",
    font=("Arial", 12, "bold"),
    bg="#eef5f2",
    fg="#333333",
    wraplength=520
)
result_label.pack(pady=25)

# --------------------------------
# 14. ANIMAL IMAGE LABEL
# --------------------------------

image_label = tk.Label(
    root,
    bg="#eef5f2"
)
image_label.pack(pady=10)

# --------------------------------
# 15. FOOTER
# --------------------------------

footer = tk.Label(
    root,
    text="AI Mini Project | Semantic Nets and Frames",
    font=("Arial", 9),
    bg="#eef5f2",
    fg="gray"
)
footer.pack(side="bottom", pady=12)

# --------------------------------
# 16. RUN APPLICATION
# --------------------------------

root.mainloop()
