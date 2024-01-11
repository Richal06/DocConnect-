# myapp/views.py
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
import threading
from django.shortcuts import render
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from .models import HeartRateData
from .forms import HeartRateForm
from django.shortcuts import render, redirect

def graph_view(request):
    return render(request, 'graph.html')
def contact(request):
    return render(request, 'shop/contact.html')

def blood(request):
    return render(request, 'blood.html')
def temp(request):
    return render(request, 'temp.html')
def pulse(request):
    return render(request, 'pulse.html')
def heart(request):
    return render(request, 'heart.html')

# def heart(request):
#     if request.method == 'POST':
#         form = HeartRateForm(request.POST)
#         if form.is_valid():
#             heart_rate = form.cleaned_data['heart_rate']
#             HeartRateData.objects.create(heart_rate=heart_rate)
#     else:
#         form = HeartRateForm()

#     heart_rate_values = HeartRateData.objects.all()
#     timestamps = [data.timestamp for data in heart_rate_values]
#     heart_rates = [data.heart_rate for data in heart_rate_values]

#     plt.figure(figsize=(10, 6))
#     plt.plot(timestamps, heart_rates, marker='o', linestyle='-', color='b')
#     plt.title("Heart Rate Over Time")
#     plt.xlabel("Time")
#     plt.ylabel("Heart Rate (bpm)")
#     plt.grid(True)

#     # Save the graph to a file (optional)
#     graph_file = 'path_to_static_directory/graph.png'
#     plt.savefig(graph_file)

#     return render(request, 'collect_data.html', {'form': form, 'graph_file': graph_file})

# # Initialize lists to store the heart rate values and timestamps
# heart_rate_values = []
# timestamps = []

# # Function to collect heart rate data and generate the graph
# def collect_data():
#     global heart_rate_values, timestamps

#     while True:
#         user_input = input("Enter heart rate (or 'q' to stop and display graph): ")

#         if user_input.lower() == 'q':
#             break

#         try:
#             heart_rate = float(user_input)
#             heart_rate_values.append(heart_rate)
#             timestamps.append(datetime.now())
#         except ValueError:
#             print("Invalid input. Please enter a numeric heart rate value.")

#         time.sleep(60 * 0.1)  # Wait for 15 minutes before collecting the next data point

#     # Plot the collected heart rate values as a line graph
#     plt.figure(figsize=(10, 6))
#     plt.plot(timestamps, heart_rate_values, marker='o', linestyle='-', color='b')
#     plt.title("Heart Rate Over Time")
#     plt.xlabel("Time")
#     plt.ylabel("Heart Rate (bpm)")
#     plt.grid(True)

#     # Convert the plot to a base64-encoded image
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plot_data = base64.b64encode(buffer.read()).decode()

#     # Embed the base64-encoded image in the HTML response
#     graph_image = f"data:image/png;base64,{plot_data}"

#     return graph_image  # Return the graph_image variable

# # Django view function to display the graph
# def graph_view(request):
#     # Get the graph_image returned by the collect_data function
#     graph_image = collect_data()

#     # Render the HTML response with the embedded graph image
#     return render(request, 'graph/graph.html', {'graph_image': graph_image})

