"""
Boundary Layer Thickness Estimation for Aft-Fuselage BLI Fan Placement
Author: Ilyasse
Date: january 2026
"""

import numpy as np

# ========================
# AIRCRAFT & FLIGHT CONDITIONS
# ========================
# Reference: ATR 72 (regional turboprop)
fuselage_length = 27.17               # meters
cruise_speed_kts = 220.0              # knots
cruise_altitude_ft = 20000            # feet

# Convert to SI
cruise_speed_ms = cruise_speed_kts * 0.5144
rho = 0.41                            # air density at 20,000 ft, kg/m³
mu = 1.63e-5                          # dynamic viscosity, kg/(m·s)

# ========================
# FAN LOCATION
# ========================
fan_position_ratio = 0.85             # 85% of fuselage length from nose
x_fan = fan_position_ratio * fuselage_length

# ========================
# REYNOLDS NUMBER
# ========================
Re_x = rho * cruise_speed_ms * x_fan / mu

# ========================
# BOUNDARY LAYER THICKNESS
# ========================
# Turbulent BL (Schlichting flat-plate approximation)
delta_turb = 0.37 * x_fan * (Re_x ** (-1/5))

# ========================
# VORTEX GENERATOR SIZING
# ========================
VG_height_ratio = 0.4                 # VG height = 40% of BL thickness
VG_height = VG_height_ratio * delta_turb

# ========================
# OUTPUT
# ========================
print("=" * 60)
print("BOUNDARY LAYER & VG INITIAL SIZING")
print("=" * 60)
print(f"Aircraft: ATR 72")
print(f"Fuselage length: {fuselage_length:.2f} m")
print(f"Cruise speed: {cruise_speed_kts} kts ({cruise_speed_ms:.1f} m/s)")
print(f"Cruise altitude: {cruise_altitude_ft} ft")
print(f"Fan location (from nose): {x_fan:.2f} m ({fan_position_ratio*100:.0f}% L)")
print(f"Reynolds number at fan location: {Re_x:.2e}")
print(f"Estimated turbulent BL thickness: {delta_turb*1000:.1f} mm")
print(f"Suggested VG height (40% of δ): {VG_height*1000:.1f} mm")
print("=" * 60)

# Optional: Save to a text file for records
with open("../docs/bl_estimation_results.txt", "w") as f:
    f.write(f"BL Thickness at x={x_fan:.2f}m: {delta_turb*1000:.1f} mm\n")
    f.write(f"VG Height Recommendation: {VG_height*1000:.1f} mm\n")
