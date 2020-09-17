# Import packages
import pandas as pd
from matplotlib.pylab import plt
import seaborn as sns

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("super_bowls.csv")
tv = pd.read_csv("tv.csv")
halftime_musicians = pd.read_csv("halftime_musicians.csv")

# display five rows of each DataFrame
# print(super_bowls.head())
# print(tv.head())
# print(halftime_musicians.head())

# Summary of the TV data to inspect
print(tv.info())
# Summary of the halftime musician data to inspect
print(halftime_musicians.info())

plt.style.use('seaborn')
# Plot a histogram of combined points
plt.hist(super_bowls.iloc[:, 16])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# print(super_bowls[super_bowls['combined_pts'] > 70])
# print(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
# print(super_bowls[super_bowls['difference_pts'] == 1])
# print(super_bowls[super_bowls['difference_pts'] >= 35])

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn

# Create a scatter plot with a linear regression model fit
sns.regplot(x=games_tv['difference_pts'], y=games_tv['share_household'], data=games_tv)

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv['super_bowl'], tv['avg_us_viewers'], color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv['super_bowl'], tv['rating_household'], '#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv['super_bowl'], tv['ad_cost'], '#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()

# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
print(halftime_musicians[halftime_musicians.super_bowl <= 27])

# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
print(halftime_appearances[halftime_appearances['super_bowl'] > 1])

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel("Number of Songs Per Halftime Show Performance")
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
print(no_bands.head(15))

# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = patriots
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)
