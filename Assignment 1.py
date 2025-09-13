# Assignment 1 - Creating the Field
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
# Official Tennis court Dimensions (in meters) 
court_length = 23.77 #baseline to baseline 
doubles_width = 10.97
singles_width = 8.23
service_line_dist = 6.40 #from net to service line 
line_width_m = 0.05 #5cm official line width 

# World - Pixel mapping 
margin_m = 2.0 #margin around court in meters 
world_width_m = doubles_width + 2 * margin_m
world_height_m = court_length + 2 * margin_m

target_max_px = 1200 # scale so longer side approx 1200 px
px_per_m = target_max_px / max(world_width_m,world_height_m)
dpi = 100
fig_w_in = (world_width_m*px_per_m) / dpi
fig_h_in = (world_height_m*px_per_m) / dpi
def linewidth_m_to_points(l_m):
    px=l_m*px_per_m
    return px*72.0/dpi #convert px to points for Matplotlib

# Draw court: 
fig, ax=plt.subplots(figsize=(fig_w_in, fig_h_in), dpi=dpi)
ax.set_xlim(-world_width_m/2, world_width_m/2)
ax.set_ylim(-world_height_m/2, world_height_m/2)
ax.set_aspect('equal')
ax.axis('off')

# Outer doubles court 
ax.add_patch(Rectangle((-doubles_width/2, -court_length/2),
                       doubles_width, court_length, 
                       fill=False, edgecolor='black', 
                       linewidth=linewidth_m_to_points(line_width_m)))

# Singles sidelines 
ax.add_line(Line2D([-singles_width/2, -singles_width/2], 
                   [-court_length/2, court_length/2],
                   color='black', linewidth=linewidth_m_to_points(line_width_m)))
ax.add_line(Line2D([singles_width/2, singles_width/2], 
                   [-court_length/2, court_length/2], 
                   color='black', linewidth=linewidth_m_to_points(line_width_m)))
# Net 
ax.add_line(Line2D([-doubles_width/2, doubles_width/2], 
                   [0,0], color='black', 
                   linestyle='--', linewidth=linewidth_m_to_points(0.02)))

#Service lines 
ax.add_line(Line2D([-singles_width/2, singles_width/2], 
                   [service_line_dist, service_line_dist], 
                   color='black', linewidth=linewidth_m_to_points(line_width_m)))
ax.add_line(Line2D([-singles_width/2, singles_width/2], 
                   [-service_line_dist, -service_line_dist], 
                   color='black', linewidth=linewidth_m_to_points(line_width_m)))

# Center Service Line 
ax.add_line(Line2D([0,0], 
                   [-service_line_dist, service_line_dist], 
                   color='black', linewidth=linewidth_m_to_points(line_width_m)))

# We want to save in PNG
output_file = "tennis_court.png"
plt.savefig(output_file, dpi=dpi, bbox_inches='tight', pad_inches=0.02)
plt.close(fig) 
print("Tennis court saved as", output_file)

