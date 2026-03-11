import tkinter as tk
from tkinter import messagebox
import random
import math
from datetime import datetime

# Constants for validation and calculations
MAX_QUANTITY = 500
BOX_SIZE = 25
DATE_FORMAT = "%d/%m/%Y"

# Lists used to store program data
hire_list = []
raffle_list = []

# Calculates how many boxes are needed
# Each box holds 25 items

def calculate_boxes(quantity):
    return math.ceil(quantity / BOX_SIZE)
