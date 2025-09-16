import matplotlib.pyplot as plt


year =[
  1950, 1960, 1970, 1980, 1990,
  2000, 2010, 2020, 2030, 2040,
  2050, 2060, 2075, 2100
]
pop =[
  2.53, 3.03, 3.70, 4.45, 5.31,
  6.12, 6.93, 7.80, 8.55, 9.20,
  9.66, 10.00, 10.25, 10.18
] 


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

#labeling the axis
plt.xlabel('<---------------     year     --------------->')
plt.ylabel('<---------------     population     --------------->')
plt.title('World Population Projection')

# Display the plot with plt.show()
plt.show()
