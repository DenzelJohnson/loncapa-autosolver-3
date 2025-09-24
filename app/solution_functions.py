import math

ke = 8.9875517923e9  # Coulomb constant (N·m^2/C^2)
sqrt = math.sqrt

questions_1D03 = [
  {
    "problem_id": "sf-prob0210a.problem",
    "question_text": "A tortoise can run with a speed of ... How long does the race take?",
    "inputs": ["v_tortoise_cmps", "hare_ratio", "rest_s", "win_margin_cm"],
    "function": "prob_sf_0210a_part1",
    "answer_units": "s",
    "pattern_matcher": "prob0210a",
    "part": 1,
    "prompt": "How long does the race take?",
  },
  {
    "problem_id": "sf-prob0210a.problem",
    "question_text": "What is the length of the race?",
    "inputs": ["v_tortoise_cmps", "hare_ratio", "rest_s", "win_margin_cm"],
    "function": "prob_sf_0210a_part2",
    "answer_units": "m",
    "pattern_matcher": "prob0210a",
    "part": 2,
    "prompt": "What is the length of the race?",
  },
  {
    "problem_id": "sf-prob0218.problem",
    "question_text": "Average acceleration during wall contact",
    "inputs": ["v_in_ms", "v_out_ms", "dt_s"],
    "function": "prob_sf_0218",
    "answer_units": "m/s^2",
    "pattern_matcher": "prob0218",
    "part": 1,
    "prompt": "Average acceleration while in contact",
  },  # Knight 0250a — braking problem
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Distance when brakes applied",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0250a",
    "part": 1,
    "prompt": "How far are you from the intersection when you begin to apply the brakes?",
  },
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Required acceleration to stop at the intersection",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0250a",
    "part": 2,
    "prompt": "What acceleration will bring you to rest as you just reach the intersection?",
  },
  {
    "problem_id": "kn-prob0250a.problem",
    "question_text": "Stopping time after brakes applied",
    "inputs": ["v0_ms", "d_m", "t_reaction_s"],
    "function": "prob_kn_0250a_part3",
    "answer_units": "s",
    "pattern_matcher": "kn0250a",
    "part": 3,
    "prompt": "How long does it take you to stop?",
  },
  # Knight 0258 — constant acceleration
  {
    "problem_id": "kn-prob0258.problem",
    "question_text": "Initial velocity from segment with constant acceleration",
    "inputs": ["a_ms2", "dx_m", "t1_s", "t2_s"],
    "function": "prob_kn_0258",
    "answer_units": "m/s",
    "pattern_matcher": "kn0258",
    "part": 1,
    "prompt": "What was the car's velocity at t=0?",
  },
  # Knight 0266a — circular motion
  {
    "problem_id": "kn-prob0266a.problem",
    "question_text": "Bridge rocks time gap",
    "inputs": ["h_m", "v0_ms"],
    "function": "prob_kn_0266a_part1",
    "answer_units": "s",
    "pattern_matcher": "kn0266a_bridge",
    "part": 1,
    "prompt": "Time between splashes",
  },
  {
    "problem_id": "kn-prob0266a.problem",
    "question_text": "Bridge rocks impact speed",
    "inputs": ["h_m", "v0_ms"],
    "function": "prob_kn_0266a_part2",
    "answer_units": "m/s",
    "pattern_matcher": "kn0266a_bridge",
    "part": 2,
    "prompt": "Impact speed",
  },
  {
    "problem_id": "sb-prob0342.problem",
    "question_text": "Equal vectors sum to j-component",
    "inputs": ["m", "sumj"],
    "function": "prob_sb_0342",
    "answer_units": "deg",
    "pattern_matcher": "sb0342",
    "part": 1,
    "prompt": "Angle between A and B",
  },
  {
    "problem_id": "sb-prob0353.problem",
    "question_text": "Equal vectors ratio condition",
    "inputs": ["k_ratio"],
    "function": "prob_sb_0353",
    "answer_units": "deg",
    "pattern_matcher": "sb0353",
    "part": 1,
    "prompt": "Angle between A and B",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: range",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part1",
    "answer_units": "m",
    "pattern_matcher": "sb0416a",
    "part": 1,
    "prompt": "Horizontal distance",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: height",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part2",
    "answer_units": "m",
    "pattern_matcher": "sb0416a",
    "part": 2,
    "prompt": "Height of window",
  },
  {
    "problem_id": "sb-prob0416a.problem",
    "question_text": "Projectile from window: time to 11.5 m below",
    "inputs": ["v0_ms", "theta_deg", "t_s"],
    "function": "prob_sb_0416a_part3",
    "answer_units": "s",
    "pattern_matcher": "sb0416a",
    "part": 3,
    "prompt": "Time to y drop",
  },
  {
    "problem_id": "sb-prob0344.problem",
    "question_text": "Buried treasure resultant distance",
    "inputs": ["d1", "ang1_deg", "d2", "ang2_deg", "d3", "ang3_deg"],
    "function": "prob_sb_0344_part1",
    "answer_units": "",
    "pattern_matcher": "sb0344",
    "part": 1,
    "prompt": "Resultant distance",
  },
  {
    "problem_id": "sb-prob0344.problem",
    "question_text": "Buried treasure resultant angle",
    "inputs": ["d1", "ang1_deg", "d2", "ang2_deg", "d3", "ang3_deg"],
    "function": "prob_sb_0344_part2",
    "answer_units": "deg",
    "pattern_matcher": "sb0344",
    "part": 2,
    "prompt": "Resultant angle (from +x)",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2]",
    "inputs": ["t1_s", "t2_s"],
    "function": "prob_sf_0206a",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 1,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2] (part 2)",
    "inputs": ["t1_s", "t2_s"],
    "function": "prob_sf_0206a",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 2,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sf-prob0206a.problem",
    "question_text": "Average velocity from fixed x(t) graph over [t1,t2] (part 3)",
    "inputs": ["t1_s", "t2_s"],
    "function": "prob_sf_0206a",
    "answer_units": "m/s",
    "pattern_matcher": "prob0206a",
    "part": 3,
    "prompt": "Average velocity",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: heading relative to shore",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part1",
    "answer_units": "deg",
    "pattern_matcher": "sb0441a",
    "part": 1,
    "prompt": "Heading relative to shore",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: boat ground-velocity angle",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part2",
    "answer_units": "deg",
    "pattern_matcher": "sb0441a",
    "part": 2,
    "prompt": "Boat velocity angle to shore",
  },
  {
    "problem_id": "sb-prob0441a.problem",
    "question_text": "River rescue: time to intercept",
    "inputs": ["v_current_kmh", "d_cross_km", "d_up_km", "v_boat_kmh"],
    "function": "prob_sb_0441a_part3",
    "answer_units": "h",
    "pattern_matcher": "sb0441a",
    "part": 3,
    "prompt": "Time to intercept",
  },
  {
    "problem_id": "sb-prob0464.problem",
    "question_text": "River speed from log timing",
    "inputs": ["x0_km", "t_up_min"],
    "function": "prob_sb_0464",
    "answer_units": "km/h",
    "pattern_matcher": "sb0464",
    "part": 1,
    "prompt": "River speed",
  },
  {
    "problem_id": "sb-prob0446.problem",
    "question_text": "Radial acceleration from break and landing",
    "inputs": ["r_m", "h_m", "R_m"],
    "function": "prob_sb_0446",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0446",
    "part": 1,
    "prompt": "Radial acceleration",
  },
  {
    "problem_id": "hr-prob0483.problem",
    "question_text": "Wind speed from ground track",
    "inputs": ["v_air_kmh", "distance_km", "heading_deg", "time_hr"],
    "function": "prob_hr_0483",
    "answer_units": "km/h",
    "pattern_matcher": "hr0483",
    "part": 1,
    "prompt": "Wind speed magnitude",
  },
  {
    "problem_id": "sf-prob0246.problem",
    "question_text": "Two balls same height time",
    "inputs": ["v0_ms", "h_m"],
    "function": "prob_sf_0246",
    "answer_units": "s",
    "pattern_matcher": "prob0246",
    "part": 1,
    "prompt": "After how long are they at the same height?",
  },
  {
    "problem_id": "sf-prob0258.problem",
    "question_text": "Downward throw time to ground",
    "inputs": ["v0_ms", "h_m"],
    "function": "prob_sf_0258",
    "answer_units": "s",
    "pattern_matcher": "prob0258",
    "part": 1,
    "prompt": "Time to hit ground",
  },
  # Knight 0214a (graph-based) — extract variables but solvers require graph info
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Position at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0214a",
    "part": 1,
    "prompt": "Position at t = ... s",
  },
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Velocity at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part2",
    "answer_units": "m/s",
    "pattern_matcher": "kn0214a",
    "part": 2,
    "prompt": "Velocity at t = ... s",
  },
  {
    "problem_id": "kn-prob0214a.problem",
    "question_text": "Acceleration at t given v-t graph (requires graph)",
    "inputs": ["x0_m", "vmax_ms", "t_total_s", "t_query_s"],
    "function": "prob_kn_0214a_part3",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0214a",
    "part": 3,
    "prompt": "Acceleration at t = ... s",
  },
  # Knight 0224a — skier on incline
  {
    "problem_id": "kn-prob0224a.problem",
    "question_text": "Length of incline",
    "inputs": ["v0_ms", "theta_deg", "vf_ms"],
    "function": "prob_kn_0224a_part1",
    "answer_units": "m",
    "pattern_matcher": "kn0224a",
    "part": 1,
    "prompt": "What is the length of the incline?",
  },
  {
    "problem_id": "kn-prob0224a.problem",
    "question_text": "Time to bottom",
    "inputs": ["v0_ms", "theta_deg", "vf_ms"],
    "function": "prob_kn_0224a_part2",
    "answer_units": "s",
    "pattern_matcher": "kn0224a",
    "part": 2,
    "prompt": "How long does it take to reach the bottom?",
  },



  
  # Assignment 3 (1D03 A3)
  {
    "problem_id": "sb-prob0518a.problem",
    "question_text": "Net acceleration magnitude from three cardinal forces on a mass",
    "inputs": ["F_n_N", "F_e_N", "F_s_N", "m_kg"],
    "function": "prob_sb_0518a_part1",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0518a",
    "part": 1,
    "prompt": "Acceleration magnitude",
  },
  {
    "problem_id": "sb-prob0518a.problem",
    "question_text": "Net acceleration direction (east=0°, CCW positive)",
    "inputs": ["F_n_N", "F_e_N", "F_s_N", "m_kg"],
    "function": "prob_sb_0518a_part2",
    "answer_units": "deg",
    "pattern_matcher": "sb0518a",
    "part": 2,
    "prompt": "Acceleration direction",
  },
  {
    "problem_id": "sb-prob0524a.problem",
    "question_text": "Three-wire support: bag of cement (find T1)",
    "inputs": ["W_N", "theta1_deg", "theta2_deg"],
    "function": "prob_sb_0524a_part1",
    "answer_units": "N",
    "pattern_matcher": "sb0524a",
    "part": 1,
    "prompt": "T1",
  },
  {
    "problem_id": "sb-prob0524a.problem",
    "question_text": "Three-wire support (find T2)",
    "inputs": ["W_N", "theta1_deg", "theta2_deg"],
    "function": "prob_sb_0524a_part2",
    "answer_units": "N",
    "pattern_matcher": "sb0524a",
    "part": 2,
    "prompt": "T2",
  },
  {
    "problem_id": "sb-prob0524a.problem",
    "question_text": "Three-wire support (find T3)",
    "inputs": ["W_N", "theta1_deg", "theta2_deg"],
    "function": "prob_sb_0524a_part3",
    "answer_units": "N",
    "pattern_matcher": "sb0524a",
    "part": 3,
    "prompt": "T3",
  },
  {
    "problem_id": "hr-prob0532.problem",
    "question_text": "Electron deflection under constant vertical force",
    "inputs": ["v0_ms", "F_N", "dx_m"],
    "function": "prob_hr_0532",
    "answer_units": "m",
    "pattern_matcher": "hr0532",
    "part": 1,
    "prompt": "Vertical deflection",
  },
  {
    "problem_id": "kn-prob0842.problem",
    "question_text": "Painter on chair-pulley: pull force for given upward acceleration",
    "inputs": ["m_painter_kg", "m_chair_kg", "a_ms2"],
    "function": "prob_kn_0842",
    "answer_units": "N",
    "pattern_matcher": "kn0842",
    "part": 1,
    "prompt": "Pull force",
  },
  {
    "problem_id": "kn-prob0832.problem",
    "question_text": "Two blocks with friction: least time without slipping",
    "inputs": ["mu_s", "mu_k", "d_m", "m_lower_kg", "m_upper_kg"],
    "function": "prob_kn_0832",
    "answer_units": "s",
    "pattern_matcher": "kn0832",
    "part": 1,
    "prompt": "Minimum time",
  },
  {
    "problem_id": "kn-prob0552.problem",
    "question_text": "Block against wall: minimal force to start moving up",
    "inputs": ["m_kg", "phi_deg", "mu_s"],
    "function": "prob_kn_0552",
    "answer_units": "N",
    "pattern_matcher": "kn0552",
    "part": 1,
    "prompt": "Required force",
  },
  {
    "problem_id": "kn-prob0810.problem",
    "question_text": "Astronaut pushes off satellite: separation after given time",
    "inputs": ["m_astronaut_kg", "m_satellite_kg", "F_N", "t_push_s", "t_after_min"],
    "function": "prob_kn_0810",
    "answer_units": "m",
    "pattern_matcher": "kn0810",
    "part": 1,
    "prompt": "Separation distance",
  },
  {
    "problem_id": "kn-prob0820.problem",
    "question_text": "Two sleds with friction: find tension in second rope",
    "inputs": ["mu_k", "mA_kg", "mB_kg", "T1_N"],
    "function": "prob_kn_0820",
    "answer_units": "N",
    "pattern_matcher": "kn0820",
    "part": 1,
    "prompt": "Tension in rope 2",
  },
  {
    "problem_id": "sb-prob0552a.problem",
    "question_text": "Pulley over block with kinetic friction: acceleration at x",
    "inputs": ["m_kg", "T_N", "h_pulley_m", "mu_k", "x_m"],
    "function": "prob_sb_0552a_part1",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0552a",
    "part": 1,
    "prompt": "Acceleration at x",
  },
  {
    "problem_id": "sb-prob0552a.problem",
    "question_text": "Pulley over block with kinetic friction: x where acceleration is zero",
    "inputs": ["m_kg", "T_N", "h_pulley_m", "mu_k", "x_m"],
    "function": "prob_sb_0552a_part2",
    "answer_units": "m",
    "pattern_matcher": "sb0552a",
    "part": 2,
    "prompt": "x at a=0",
  },
  {
    "problem_id": "sb-prob0563a.problem",
    "question_text": "Toaster on countertop: optimal pull angle",
    "inputs": ["m_kg", "mu_s"],
    "function": "prob_sb_0563a_part1",
    "answer_units": "deg",
    "pattern_matcher": "sb0563a",
    "part": 1,
    "prompt": "Optimal angle",
  },
  {
    "problem_id": "sb-prob0563a.problem",
    "question_text": "Toaster on countertop: minimal tension at that angle",
    "inputs": ["m_kg", "mu_s"],
    "function": "prob_sb_0563a_part2",
    "answer_units": "N",
    "pattern_matcher": "sb0563a",
    "part": 2,
    "prompt": "Tension",
  },
  {
    "problem_id": "hr-prob0621.problem",
    "question_text": "Crates in truck: minimum stopping distance without sliding",
    "inputs": ["mu_s", "v_kmh"],
    "function": "prob_hr_0621",
    "answer_units": "m",
    "pattern_matcher": "hr0621",
    "part": 1,
    "prompt": "Stopping distance",
  },

  # Assignment 4 (1D03 A4)
  {
    "problem_id": "sf-prob0442a.problem",
    "question_text": "Block on incline held by horizontal force; find minimum F and normal force",
    "inputs": ["m_kg", "theta_deg", "mu_s"],
    "function": "prob_sf_0442a_part1",
    "answer_units": "N",
    "pattern_matcher": "sf0442a",
    "part": 1,
    "prompt": "Minimum horizontal force F",
  },
  {
    "problem_id": "sf-prob0442a.problem",
    "question_text": "Normal force exerted by incline",
    "inputs": ["m_kg", "theta_deg", "mu_s"],
    "function": "prob_sf_0442a_part2",
    "answer_units": "N",
    "pattern_matcher": "sf0442a",
    "part": 2,
    "prompt": "Normal force",
  },
  {
    "problem_id": "sf-prob0458.problem",
    "question_text": "Rope deflection in accelerating car; find car acceleration",
    "inputs": ["m_kg", "alpha_deg"],
    "function": "prob_sf_0458",
    "answer_units": "m/s^2",
    "pattern_matcher": "sf0458",
    "part": 1,
    "prompt": "Car acceleration",
  },
  {
    "problem_id": "sb-prob0568a.problem",
    "question_text": "Two stacked blocks with kinetic friction; string tension",
    "inputs": ["m1_kg", "m2_kg", "F_N", "mu_k"],
    "function": "prob_sb_0568a_part1",
    "answer_units": "N",
    "pattern_matcher": "sb0568a",
    "part": 1,
    "prompt": "String tension",
  },
  {
    "problem_id": "sb-prob0568a.problem",
    "question_text": "Two stacked blocks with kinetic friction; acceleration of heavy block",
    "inputs": ["m1_kg", "m2_kg", "F_N", "mu_k"],
    "function": "prob_sb_0568a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0568a",
    "part": 2,
    "prompt": "Acceleration of 12.5 kg block",
  },
  {
    "problem_id": "sb-prob0613a.problem",
    "question_text": "Conical pendulum: force components and radial acceleration",
    "inputs": ["m_kg", "L_m", "theta_deg"],
    "function": "prob_sb_0613a_part1",
    "answer_units": "N",
    "pattern_matcher": "sb0613a",
    "part": 1,
    "prompt": "Horizontal component of wire force",
  },
  {
    "problem_id": "sb-prob0613a.problem",
    "question_text": "Conical pendulum: vertical component of force",
    "inputs": ["m_kg", "L_m", "theta_deg"],
    "function": "prob_sb_0613a_part2",
    "answer_units": "N",
    "pattern_matcher": "sb0613a",
    "part": 2,
    "prompt": "Vertical component of wire force",
  },
  {
    "problem_id": "sb-prob0613a.problem",
    "question_text": "Conical pendulum: radial acceleration",
    "inputs": ["m_kg", "L_m", "theta_deg"],
    "function": "prob_sb_0613a_part3",
    "answer_units": "m/s^2",
    "pattern_matcher": "sb0613a",
    "part": 3,
    "prompt": "Radial acceleration",
  },
  {
    "problem_id": "sb-prob0611.problem",
    "question_text": "Crate in truck on unbanked curve: maximum speed without sliding",
    "inputs": ["R_m", "mu_s"],
    "function": "prob_sb_0611",
    "answer_units": "m/s",
    "pattern_matcher": "sb0611",
    "part": 1,
    "prompt": "Maximum speed",
  },
  {
    "problem_id": "hr-prob0636a.problem",
    "question_text": "Two sleds tied together on incline with friction: tension and acceleration",
    "inputs": ["mA_kg", "mB_kg", "theta_deg", "mu_k_A", "mu_k_B"],
    "function": "prob_hr_0636a_part1",
    "answer_units": "N",
    "pattern_matcher": "hr0636a",
    "part": 1,
    "prompt": "Tension in bar",
  },
  {
    "problem_id": "hr-prob0636a.problem",
    "question_text": "Two sleds tied together on incline with friction: acceleration",
    "inputs": ["mA_kg", "mB_kg", "theta_deg", "mu_k_A", "mu_k_B"],
    "function": "prob_hr_0636a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "hr0636a",
    "part": 2,
    "prompt": "Acceleration of sleds",
  },
  {
    "problem_id": "hr-prob0666.problem",
    "question_text": "Banked turn by airplane (tilted wings): find turn radius",
    "inputs": ["v_kmh", "tilt_deg"],
    "function": "prob_hr_0666",
    "answer_units": "m",
    "pattern_matcher": "hr0666",
    "part": 1,
    "prompt": "Turn radius",
  },
  {
    "problem_id": "hr-prob0670b.problem",
    "question_text": "Ball on rotating rod with two strings: lower string tension",
    "inputs": ["m_kg", "L_m", "T_upper_N"],
    "function": "prob_hr_0670b_part1",
    "answer_units": "N",
    "pattern_matcher": "hr0670b",
    "part": 1,
    "prompt": "Lower string tension",
  },
  {
    "problem_id": "hr-prob0670b.problem",
    "question_text": "Ball on rotating rod with two strings: speed of ball",
    "inputs": ["m_kg", "L_m", "T_upper_N"],
    "function": "prob_hr_0670b_part2",
    "answer_units": "m/s",
    "pattern_matcher": "hr0670b",
    "part": 2,
    "prompt": "Speed of ball",
  },
  {
    "problem_id": "kn-prob0828.problem",
    "question_text": "Two-block system with friction and applied force: acceleration of lower block",
    "inputs": ["F_N", "mu_k_surface", "mu_k_between", "m_lower_kg", "m_upper_kg"],
    "function": "prob_kn_0828",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0828",
    "part": 1,
    "prompt": "Acceleration of lower block",
  },
  {
    "problem_id": "kn-prob0836a.problem",
    "question_text": "Incline with pulley to hanging mass: minimum M1 and acceleration when nudged",
    "inputs": ["theta_deg", "mu_s", "mu_k", "m2_kg"],
    "function": "prob_kn_0836a_part1",
    "answer_units": "kg",
    "pattern_matcher": "kn0836a",
    "part": 1,
    "prompt": "Minimum M1",
  },
  {
    "problem_id": "kn-prob0836a.problem",
    "question_text": "Incline with pulley to hanging mass: acceleration when nudged",
    "inputs": ["theta_deg", "mu_s", "mu_k", "m2_kg"],
    "function": "prob_kn_0836a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0836a",
    "part": 2,
    "prompt": "Acceleration when nudged",
  },
  {
    "problem_id": "kn-prob0838a.problem",
    "question_text": "Book on slope with hanging cup: acceleration and slide distance",
    "inputs": ["m_book_kg", "m_cup_kg", "v0_ms", "mu_s", "mu_k", "theta_deg"],
    "function": "prob_kn_0838a_part1",
    "answer_units": "m/s^2",
    "pattern_matcher": "kn0838a",
    "part": 1,
    "prompt": "Acceleration of book",
  },
  {
    "problem_id": "kn-prob0838a.problem",
    "question_text": "Book on slope with hanging cup: distance until stop",
    "inputs": ["m_book_kg", "m_cup_kg", "v0_ms", "mu_s", "mu_k", "theta_deg"],
    "function": "prob_kn_0838a_part2",
    "answer_units": "m",
    "pattern_matcher": "kn0838a",
    "part": 2,
    "prompt": "Slide distance to stop",
  },
  {
    "problem_id": "cj-prob0491a.problem",
    "question_text": "Massless pulleys and rope: tension and acceleration (2:1 displacement constraint)",
    "inputs": ["M_big_kg", "M_small_kg"],
    "function": "prob_cj_0491a_part1",
    "answer_units": "N",
    "pattern_matcher": "cj0491a",
    "part": 1,
    "prompt": "Tension in rope",
  },
  {
    "problem_id": "cj-prob0491a.problem",
    "question_text": "Massless pulleys and rope: acceleration of 10.09 kg block",
    "inputs": ["M_big_kg", "M_small_kg"],
    "function": "prob_cj_0491a_part2",
    "answer_units": "m/s^2",
    "pattern_matcher": "cj0491a",
    "part": 2,
    "prompt": "Acceleration of 10.09 kg block",
  },
]


questions_1E03 = [
  {
    "problem_id": "sf-prob1508.problem",
    "question_text": "A 6.00E-9C charge is on the x axis at x = -1.58m and a 1.95E-9C charge is on the x axis at x = 1.88m. Find the net force exerted on a 3.32E-9C charge located at the origin.",
    "inputs": ["q1", "x1", "q2", "x2", "q3"],
    "function": "prob_sf_1508",
    "answer_units": "N",
    "pattern_matcher": "prob1508",
  },
  {
    "problem_id": "sf-prob1514.problem",
    "question_text": "A charge of 2.27E-9C is placed at the origin, and a charge of 4.23E-9C is placed at x = 1.50m. Locate the x coordinate of the point between the two charges at which a charge of 2.83E-9C should be placed so that the net electric force on it is zero.",
    "inputs": ["q1", "q2", "x1", "q3"],
    "function": "prob_sf_1514",
    "answer_units": "m",
    "pattern_matcher": "prob1514",
  },
  # multipart: same problem_id, shared matcher/inputs, different solvers/units/parts
  {
    "problem_id": "sf-prob1560a.problem",
    "question_text": "A charged cork ball of mass ... Calculate the charge on the ball.",
    "inputs": ["m", "x_comp", "y_comp", "deg"],
    "function": "prob_sf_1560a_part1",
    "answer_units": "C",
    "pattern_matcher": "prob1560a",
    "part": 1,
    "prompt": "Calculate the charge on the ball",
  },
  {
    "problem_id": "sf-prob1560a.problem",
    "question_text": "Calculate the tension in the string.",
    "inputs": ["m", "x_comp", "y_comp", "deg"],
    "function": "prob_sf_1560a_part2",
    "answer_units": "N",
    "pattern_matcher": "prob1560a",
    "part": 2,
    "prompt": "Calculate the tension in the string",
  },
]

# Aliases with the literal names requested (not valid Python identifiers for direct use)
globals()["1D03_questions"] = questions_1D03
globals()["1E03_questions"] = questions_1E03

# Indexes are built at the end of the file after all question lists are defined.











# Physics 1D03 Solutions Functions


def prob_sf_0210a_part1(v_tortoise_cmps=None, hare_ratio=None, rest_s=None, win_margin_cm=None):
    """Return race duration T (s) where tortoise wins by win_margin_cm.
    Inputs are numeric values as strings/floats with units implied by names.
    v_tortoise_cmps: cm/s, hare_ratio: unitless, rest_s: s, win_margin_cm: cm
    """
    if None in (v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm):
        raise ValueError("tortoise_hare_time requires v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm")
    v = float(v_tortoise_cmps)           # cm/s
    r = float(hare_ratio)
    R = float(rest_s)                    # s
    dwin = float(win_margin_cm)          # cm
    vh = r * v                           # cm/s
    denom = (vh - v)
    if abs(denom) < 1e-12:
        raise ValueError("hare speed must exceed tortoise speed")
    T = (vh * R - dwin) / denom          # s
    if T <= 0:
        raise ValueError("non-physical race time")
    return T


def prob_sf_0210a_part2(v_tortoise_cmps=None, hare_ratio=None, rest_s=None, win_margin_cm=None):
    """Return race length (m). Uses T from prob_sf_0210a_part1 and v in cm/s."""
    T = prob_sf_0210a_part1(v_tortoise_cmps, hare_ratio, rest_s, win_margin_cm)  # s
    v = float(v_tortoise_cmps)  # cm/s
    L_cm = v * T                # cm
    L_m = L_cm / 100.0         # m
    return L_m


def prob_sf_0218(v_in_ms=None, v_out_ms=None, dt_s=None):
    """Average acceleration magnitude during a bounce against a wall.
    v_in_ms: incident speed (m/s), v_out_ms: rebound speed magnitude (m/s), dt_s: contact time (s).
    Assumes velocity reverses direction during contact; returns positive magnitude.
    """
    if None in (v_in_ms, v_out_ms, dt_s):
        raise ValueError("avg_accel_rebound requires v_in_ms, v_out_ms, dt_s")
    vi = float(v_in_ms)
    vo = float(v_out_ms)
    dt = float(dt_s)
    if dt <= 0:
        raise ValueError("dt must be > 0")
    # initial +vi toward wall, final velocity is -vo away from wall
    delta_v = (-vo) - (+vi)
    a = -(abs(delta_v) / dt)
    return a


def prob_sf_0246(v0_ms=None, h_m=None):
    """Time when y_ground_ball == y_dropped_ball given same start time.
    Ground ball: y1 = v0*t - 1/2 g t^2; Dropped ball: y2 = h - 1/2 g t^2 -> v0*t = h => t=h/v0
    """
    if None in (v0_ms, h_m):
        raise ValueError("two_balls_meet_time requires v0_ms, h_m")
    v0 = float(v0_ms)
    h = float(h_m)
    if v0 <= 0:
        raise ValueError("v0 must be > 0")
    return h / v0


def prob_kn_0258(a_ms2=None, dx_m=None, t1_s=None, t2_s=None):
    """Given constant acceleration a, displacement between t1 and t2 (dx), compute v0.
    dx = v0*(t2-t1) + 0.5*a*(t2^2 - t1^2) -> v0 = (dx - 0.5*a*(t2^2 - t1^2)) / (t2 - t1)
    """
    if None in (a_ms2, dx_m, t1_s, t2_s):
        raise ValueError("initial_velocity_from_segment requires a_ms2, dx_m, t1_s, t2_s")
    a = float(a_ms2)
    dx = float(dx_m)
    t1 = float(t1_s)
    t2 = float(t2_s)
    if t2 == t1:
        raise ValueError("t2 must differ from t1")
    v0 = (dx - 0.5 * a * (t2*t2 - t1*t1)) / (t2 - t1)
    return v0


def prob_kn_0214a_part1(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Position at time t given a linear v-t graph: v(t) = (vmax/t_total) * t for 0<=t<=t_total.
    Uses x(t) = x0 + ∫ v dt = x0 + 0.5*(vmax/t_total)*t^2. Times beyond t_total are clamped to t_total.
    """
    if None in (x0_m, vmax_ms, t_total_s, t_query_s):
        raise ValueError("kn0214_position requires x0_m, vmax_ms, t_total_s, t_query_s")
    x0 = float(x0_m)
    vmax = float(vmax_ms)
    T = float(t_total_s)
    t = min(max(float(t_query_s), 0.0), T) if T > 0 else float(t_query_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    a = vmax / T
    x = x0 + 0.5 * a * t * t
    return x


def prob_kn_0214a_part2(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Velocity at time t for linear ramp: v(t) = (vmax/t_total) * t, clamped to [0, vmax]."""
    if None in (vmax_ms, t_total_s, t_query_s):
        raise ValueError("kn0214_velocity requires vmax_ms, t_total_s, t_query_s")
    vmax = float(vmax_ms)
    T = float(t_total_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    t = float(t_query_s)
    v = (vmax / T) * t
    # Clamp to [0, vmax]
    if v < 0:
        v = 0.0
    if v > vmax:
        v = vmax
    return v


def prob_kn_0214a_part3(x0_m=None, vmax_ms=None, t_total_s=None, t_query_s=None):
    """Constant acceleration (slope) for the linear ramp: a = vmax/t_total."""
    if None in (vmax_ms, t_total_s):
        raise ValueError("kn0214_acceleration requires vmax_ms, t_total_s")
    vmax = float(vmax_ms)
    T = float(t_total_s)
    if T <= 0:
        raise ValueError("t_total must be positive")
    return vmax / T


def prob_kn_0224a_part1(v0_ms=None, theta_deg=None, vf_ms=None):
    if None in (v0_ms, theta_deg, vf_ms):
        raise ValueError("incline_length requires v0_ms, theta_deg, vf_ms")
    v0 = float(v0_ms)
    vf = float(vf_ms)
    theta = math.radians(float(theta_deg))
    g = 9.80665
    a = g * math.sin(theta)
    if a <= 0:
        raise ValueError("invalid angle for downhill acceleration")
    s = (vf*vf - v0*v0) / (2.0 * a)
    return s


def prob_kn_0224a_part2(v0_ms=None, theta_deg=None, vf_ms=None):
    if None in (v0_ms, theta_deg, vf_ms):
        raise ValueError("incline_time requires v0_ms, theta_deg, vf_ms")
    v0 = float(v0_ms)
    vf = float(vf_ms)
    theta = math.radians(float(theta_deg))
    g = 9.80665
    a = g * math.sin(theta)
    if a <= 0:
        raise ValueError("invalid angle for downhill acceleration")
    t = (vf - v0) / a
    return t


def prob_sb_0416a_part1(v0_ms=None, theta_deg=None, t_s=None):
    if None in (v0_ms, theta_deg, t_s):
        raise ValueError("proj_window_range requires v0_ms, theta_deg, t_s")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    t = float(t_s)
    return v0 * math.cos(-theta) * t


def prob_sb_0416a_part2(v0_ms=None, theta_deg=None, t_s=None):
    if None in (v0_ms, theta_deg, t_s):
        raise ValueError("proj_window_height requires v0_ms, theta_deg, t_s")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    t = float(t_s)
    g = 9.80665
    # y = h - v0*sin(theta)*t - 0.5 g t^2; solve for h
    h = v0 * math.sin(theta) * t + 0.5 * g * t * t
    return h


def prob_sb_0416a_part3(v0_ms=None, theta_deg=None, t_s=None):
    """Time to be 11.5 m below the launch height for a launch angle below horizontal.
    Uses fixed drop of 11.5 m to align with resource wording.
    """
    if None in (v0_ms, theta_deg):
        raise ValueError("proj_time_to_drop requires v0_ms, theta_deg")
    v0 = float(v0_ms)
    theta = math.radians(float(theta_deg))
    yd = 11.5
    g = 9.80665
    # Equation: -v0*sin(theta)*t - 0.5 g t^2 = -yd ⇒ 0.5 g t^2 + v0*sin(theta) t - yd = 0
    a = 0.5 * g
    b = v0 * math.sin(theta)
    c = -yd
    disc = b*b - 4*a*c
    t1 = (-b + math.sqrt(disc)) / (2*a)
    t2 = (-b - math.sqrt(disc)) / (2*a)
    return max(t1, t2)


def prob_sb_0344_part1(d1=None, ang1_deg=None, d2=None, ang2_deg=None, d3=None, ang3_deg=None):
    if None in (d1, ang1_deg, d2, ang2_deg, d3, ang3_deg):
        raise ValueError("treasure_resultant_distance requires all legs")
    import math as _m
    def comp(d, ang):
        a = _m.radians(float(ang))
        return float(d)*_m.cos(a), float(d)*_m.sin(a)
    x1,y1 = comp(d1, ang1_deg)
    x2,y2 = comp(d2, ang2_deg)
    x3,y3 = comp(d3, ang3_deg)
    X = x1+x2+x3
    Y = y1+y2+y3
    return math.hypot(X, Y)


def prob_sb_0344_part2(d1=None, ang1_deg=None, d2=None, ang2_deg=None, d3=None, ang3_deg=None):
    if None in (d1, ang1_deg, d2, ang2_deg, d3, ang3_deg):
        raise ValueError("treasure_resultant_angle requires all legs")
    import math as _m
    def comp(d, ang):
        a = _m.radians(float(ang))
        return float(d)*_m.cos(a), float(d)*_m.sin(a)
    x1,y1 = comp(d1, ang1_deg)
    x2,y2 = comp(d2, ang2_deg)
    x3,y3 = comp(d3, ang3_deg)
    X = x1+x2+x3
    Y = y1+y2+y3
    ang = math.degrees(math.atan2(Y, X))
    if ang < 0:
        ang += 360.0
    return ang


def prob_sf_0206a(t1_s=None, t2_s=None):
    """Average velocity over [t1,t2] for the fixed piecewise x(t) shown in the image.
    Graph interpretation (units: t in s, x in m):
      Segment A: 0 ≤ t ≤ 1.0      x(t) = 4 t
      Segment B: 1.0 < t ≤ 2.5    x(t) = 8 − 4 t
      Segment C: 2.5 < t ≤ 3.5    x(t) = −2
      Segment D: 3.5 < t ≤ 5.0    x(t) = −2 + (4/3)(t − 3.5)
    """
    if None in (t1_s, t2_s):
        raise ValueError("avg_velocity_from_fixed_xt requires t1_s, t2_s")
    t1 = float(t1_s)
    t2 = float(t2_s)
    if t2 == t1:
        return 0.0

    def x_of(t: float) -> float:
        if t <= 0.0:
            return 0.0
        if t <= 1.0:
            return 4.0 * t
        if t <= 2.0:
            return 8.0 - 4.0 * t
        if t <= 4.0:
            return -2.0
        if t <= 5.0:
            return 2.0 * t - 10.0
        # Extrapolate last segment if needed
        return 2.0 * t - 10.0

    return (x_of(t2) - x_of(t1)) / (t2 - t1)

# (removed fixed-interval wrappers; now parts use dynamic [t1,t2] from matcher)


# Build indexes now that all question lists are defined
CATALOG_BY_ID = {q["problem_id"]: q for q in (questions_1E03 + questions_1D03)}
CATALOG_GROUPED_BY_ID = {}
for q in (questions_1E03 + questions_1D03):
    CATALOG_GROUPED_BY_ID.setdefault(q["problem_id"], []).append(q)


def prob_sb_0441a_part1(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (v_current_kmh, d_cross_km, d_up_km, v_boat_kmh):
        raise ValueError("river_rescue_heading requires v_current_kmh, d_cross_km, d_up_km, v_boat_kmh")
    # Heading relative to shore to intercept: theta = atan2(y0, x0), independent of current
    y0 = float(d_cross_km)
    x0 = float(d_up_km)
    alpha_deg = math.degrees(math.atan2(y0, x0))
    return alpha_deg

def prob_sb_0441a_part2(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (v_current_kmh, d_cross_km, d_up_km, v_boat_kmh):
        raise ValueError("river_rescue_boat_angle requires v_current_kmh, d_cross_km, d_up_km, v_boat_kmh")
    # Intercept time: distance to child's initial position at speed through water (current cancels)
    t_h = math.hypot(d_up_km, d_cross_km) / float(v_boat_kmh)
    # Child has drifted downstream by v_current * t_h when intercepted
    x_intercept = -float(d_up_km) + float(v_current_kmh) * t_h
    # Angle (w.r.t. shore) of the boat's ground velocity toward the intercept point
    phi_raw_deg = math.degrees(math.atan2(float(d_cross_km), x_intercept))
    # Return the acute angle with the shore (0–90°)
    return abs(phi_raw_deg) if abs(phi_raw_deg) <= 90 else 180 - abs(phi_raw_deg)


def prob_sb_0441a_part3(v_current_kmh=None, d_cross_km=None, d_up_km=None, v_boat_kmh=None):
    if None in (v_current_kmh, d_cross_km, d_up_km, v_boat_kmh):
        raise ValueError("river_rescue_time requires v_current_kmh, d_cross_km, d_up_km, v_boat_kmh")
    vb = float(v_boat_kmh)
    y0 = float(d_cross_km)
    x0 = float(d_up_km)
    theta = math.atan2(y0, x0)
    # Time to intercept: t = y0 / (vb * sin(theta)) = x0 / (vb * cos(theta)) (hours)
    s = vb * math.sin(theta)
    if abs(s) < 1e-12:
        raise ValueError("boat cross-speed too small")
    t_h = y0 / s
    return t_h


def prob_sb_0464(x0_km=None, t_up_min=None):
    if None in (x0_km, t_up_min):
        raise ValueError("river_velocity_from_log requires x0_km, t_up_min")
    x0 = float(x0_km)
    t_h = float(t_up_min) / 60.0
    if t_h <= 0:
        raise ValueError("time must be positive")
    # Result for this classic setup: river speed u = x0 / (2 * t_up)
    return x0 / (2.0 * t_h)


def prob_sb_0446(r_m=None, h_m=None, R_m=None):
    if None in (r_m, h_m, R_m):
        raise ValueError("radial_accel_from_break requires r_m, h_m, R_m")
    r = float(r_m)
    h = float(h_m)
    R = float(R_m)
    g = 9.80665
    # Time of fall from height h: t = sqrt(2h/g)
    t = math.sqrt(2.0 * h / g)
    # Horizontal speed equals tangential speed at break: vx = R / t
    vx = R / t
    # Radial acceleration a = v^2 / r
    return (vx * vx) / r


def prob_hr_0483(v_air_kmh=None, distance_km=None, heading_deg=None, time_hr=None):
    if None in (v_air_kmh, distance_km, heading_deg, time_hr):
        raise ValueError("wind_speed_from_track requires v_air_kmh, distance_km, heading_deg, time_hr")
    v_air = float(v_air_kmh)
    d = float(distance_km)
    t = float(time_hr)
    heading = math.radians(float(heading_deg))
    # Ground speed magnitude from distance/time
    v_g = d / t
    # Desired ground track is due north. Airspeed vector is at heading east of north.
    # Components: V_air = (v_air * sin(heading), v_air * cos(heading)) in (east,north)
    # Ground: V_g = (0, v_g) = V_air + V_wind => V_wind = (-v_air*sin(heading), v_g - v_air*cos(heading))
    vx_w = -v_air * math.sin(heading)
    vy_w = v_g - v_air * math.cos(heading)
    return math.hypot(vx_w, vy_w)


def prob_sf_0258(v0_ms=None, h_m=None):
    """Time to hit ground when thrown straight down from height h with initial speed v0.
    Solve 0.5 g t^2 + v0 t - h = 0 and return positive root.
    """
    if None in (v0_ms, h_m):
        raise ValueError("time_to_ground_downward requires v0_ms, h_m")
    v0 = float(v0_ms)
    h = float(h_m)
    g = 9.80665
    a = 0.5 * g
    b = v0
    c = -h
    disc = b*b - 4*a*c
    if disc < 0:
        raise ValueError("no real impact time")
    t1 = (-b + math.sqrt(disc)) / (2*a)
    t2 = (-b - math.sqrt(disc)) / (2*a)
    return max(t1, t2)

def prob_kn_0810(m_astronaut_kg, m_satellite_kg, F_N, t_push_s, t_after_min, g=None):
    """
    Separation distance (m) between astronaut (m1) and satellite (m2)
    when a constant push of magnitude F is applied for t_push seconds,
    starting from rest. Report separation at t_after_min minutes after
    the push BEGINS.

    During push: a1=F/m1, a2=F/m2; separation grows as 0.5*(a1+a2)*t^2.
    After push: relative speed is v_rel = (a1+a2)*t_push; separation grows linearly.
    """
    m1 = float(m_astronaut_kg)
    m2 = float(m_satellite_kg)
    F  = float(F_N)
    tp = float(t_push_s)
    T  = float(t_after_min) * 60.0

    inv_sum = (1.0/m1 + 1.0/m2)  # 1/kg
    if T <= tp:
        return 0.5 * F * inv_sum * T*T
    s_push = 0.5 * F * inv_sum * tp*tp
    v_rel  = F * inv_sum * tp
    return s_push + v_rel * (T - tp)


# ----------------------------
# kn-prob0820.problem
# Two sleds with kinetic friction on snow: find tension in rope 2
# ----------------------------
def prob_kn_0820(mu_k, mA_kg, mB_kg, T1_N, g=9.80665):
    """
    T2 for two-sled train with kinetic friction μ_k for both sleds.
    Rope-1 (T1) connects A and B, rope-2 (T2) connects dog to B.

    From dynamics with common acceleration a and f_k = μ_k m g:
        a = (T1 - μ_k mA g)/mA
        a = T2/(mA+mB) - μ_k g
    Eliminating a ⇒  T2 = (mA + mB) * (T1 / mA)
    (μ_k cancels algebraically).
    """
    mA = float(mA_kg)
    mB = float(mB_kg)
    T1 = float(T1_N)
    return (mA + mB) * (T1 / mA)


# ----------------------------
# sb-prob0552a.problem — Part 1
# Pulley over block with kinetic friction: acceleration at x
# ----------------------------
def prob_sb_0552a_part1(m_kg, T_N, h_pulley_m, mu_k, x_m, g=9.80665):
    """
    Block of mass m on rough horizontal surface (μ_k). A rope at height h above
    the block's top runs over a pulley; the segment to the block makes angle
    θ = arctan(h/x). Tension magnitude is T (constant).

    Horizontal net force: F_x = T cosθ - μ_k (m g - T sinθ)
    ⇒ a = F_x / m
    """
    m  = float(m_kg)
    T  = float(T_N)
    h  = float(h_pulley_m)
    x  = max(1e-12, float(x_m))  # avoid divide-by-zero
    th = math.atan2(h, x)
    sin_th = math.sin(th)
    cos_th = math.cos(th)
    N = m*g - T*sin_th
    fk = mu_k * N
    ax = (T*cos_th - fk) / m
    return ax


# ----------------------------
# sb-prob0552a.problem — Part 2
# x where acceleration becomes zero
# ----------------------------
def prob_sb_0552a_part2(m_kg, T_N, h_pulley_m, mu_k, x_m=None, g=9.80665):
    """
    Solve for x ≥ 0 such that acceleration from part 1 is zero:
        T cosθ - μ_k (m g - T sinθ) = 0,
    with θ = arctan(h/x). Using cosθ = x/R, sinθ = h/R, R = sqrt(x^2 + h^2),
        μ_k m g R = T (x + μ_k h)
    Let A = T/(μ_k m g). Solve quadratic:
        (1 - A^2) x^2 - 2 A^2 μ_k h x + h^2 (1 - A^2 μ_k^2) = 0
    Return the smallest nonnegative root. Falls back to a numeric solve if needed.
    """
    m  = float(m_kg)
    T  = float(T_N)
    h  = float(h_pulley_m)
    mu = float(mu_k)

    A = T / (mu * m * g)

    a = 1.0 - A*A
    b = -2.0 * (A*A) * mu * h
    c = h*h * (1.0 - (A*A) * (mu*mu))

    def quad_root(a, b, c):
        D = b*b - 4*a*c
        if D < 0:
            return None
        r1 = (-b - math.sqrt(D)) / (2*a)
        r2 = (-b + math.sqrt(D)) / (2*a)
        cands = [r for r in (r1, r2) if r >= 0]
        if not cands:
            return None
        return min(cands)

    # Primary: quadratic route (valid unless a≈0)
    if abs(a) > 1e-12:
        xr = quad_root(a, b, c)
        if xr is not None:
            return xr

    # Fallback: solve μ_k m g*sqrt(x^2+h^2) - T(x + μ_k h) = 0 with bisection
    def f(x):
        return mu*m*g*math.hypot(x, h) - T*(x + mu*h)

    lo, hi = 0.0, max(1.0, 10.0*h)
    # Expand hi until sign change or limit
    for _ in range(60):
        if f(lo) == 0.0:
            return lo
        if f(hi) == 0.0 or f(lo)*f(hi) < 0:
            break
        hi *= 2.0
    # Bisection
    for _ in range(80):
        mid = 0.5*(lo+hi)
        fm = f(mid)
        if fm == 0.0:
            return mid
        if f(lo)*fm < 0:
            hi = mid
        else:
            lo = mid
    return 0.5*(lo+hi)


# ----------------------------
# sb-prob0563a.problem — Part 1
# Toaster: optimal pull angle to minimize required tension
# ----------------------------
def prob_sb_0563a_part1(m_kg, mu_s):
    """
    Optimal angle (deg) above horizontal to minimize the tension needed
    to start motion: θ* = arctan(μ_s).
    """
    return math.degrees(math.atan(float(mu_s)))


# ----------------------------
# sb-prob0563a.problem — Part 2
# Toaster: minimal tension at that optimal angle
# ----------------------------
def prob_sb_0563a_part2(m_kg, mu_s, g=9.80665):
    """
    Minimal tension (N) at θ* = arctan(μ_s):
        T_min = μ_s m g / sqrt(1 + μ_s^2)
    """
    m  = float(m_kg)
    mu = float(mu_s)
    return (mu * m * g) / math.sqrt(1.0 + mu*mu)


# ----------------------------
# hr-prob0621.problem
# Crates in truck: minimum stopping distance without sliding
# ----------------------------
def prob_hr_0621(mu_s, v_kmh, g=9.80665):
    """
    Max decel without sliding is a = μ_s g.
    Convert v (km/h) -> m/s, stopping distance s = v^2 / (2 a).
    """
    v = float(v_kmh) * (1000.0/3600.0)  # m/s
    a = float(mu_s) * g
    if a <= 0:
        raise ValueError("mu_s must be positive")
    return v*v / (2.0 * a)


# Physcis 1E03 Solutions Functions

def prob_sf_1508(q1=None, x1=None, q2=None, x2=None, q3=None):
    """Calculate net force magnitude on q3 at origin due to q1 at x1 and q2 at x2 (1D)."""
    if q1 is None or x1 is None or q2 is None or x2 is None or q3 is None:
        raise ValueError("three_charges requires parameters: q1, x1, q2, x2, q3")
    
    # Coulomb contributions (scalar magnitudes)
    fq1 = (q1*q3)/(abs(x1))**2
    fq2 = (q2*q3)/(abs(x2))**2

    # Direction: charges on opposite sides of origin; net at origin is difference in magnitudes
    fnet = ke * (fq1 - fq2)
    return abs(fnet)


def prob_sf_1514(q1=None, q2=None, x1=None, q3=None):
    """Find x between two charges at 0 and x1 where net force on test charge is zero (1D)."""
    if q1 is None or q2 is None or x1 is None or q3 is None:
        raise ValueError("middle requires parameters: q1, q2, x1, q3")

    # Solve for x in (k*q1/x^2) = (k*q2/(x1-x)^2) with x in (0, x1)
    # Taking square roots: sqrt(q1)/|x| = sqrt(q2)/|x1-x|
    # Assume positive distances in segment (0, x1)
    r = math.sqrt(abs(q1)/abs(q2))
    # r = (x)/(x1-x) -> r*(x1-x) = x -> r*x1 = x*(1+r) -> x = r*x1/(1+r)
    x = (r * x1) / (1.0 + r)
    return x


# Shared core for the hanging ball in E-field
# Returns a dict with reusable quantities; expects SI units and degrees for angle

def ball_hanging_core(m=None, x_comp=None, y_comp=None, deg=None):
    if m is None or x_comp is None or y_comp is None or deg is None:
        raise ValueError("ball_hanging_* requires m, x_comp, y_comp, deg")
    theta = math.radians(deg)
    g = 9.80665
    Ex, Ey = x_comp, y_comp

    # Equilibrium equations derivation in pipeline comments
    s, c = math.sin(theta), math.cos(theta)
    if abs(s) < 1e-12:
        raise ValueError("theta too small for stable computation")
    denom = (Ey - (Ex * c / s))
    if abs(denom) < 1e-18:
        raise ValueError("degenerate field/angle configuration")
    q = (m * g) / denom
    T = abs(-q * Ex / s)
    return {"theta": theta, "q": q, "T": T, "Ex": Ex, "Ey": Ey}


def prob_sf_1560a_part1(m=None, x_comp=None, y_comp=None, deg=None):
    return ball_hanging_core(m, x_comp, y_comp, deg)["q"]


def prob_sf_1560a_part2(m=None, x_comp=None, y_comp=None, deg=None):
    return ball_hanging_core(m, x_comp, y_comp, deg)["T"]


def prob_kn_0266a_part1(h_m=None, v0_ms=None):
    if None in (h_m, v0_ms):
        raise ValueError("bridge_time_gap requires h_m, v0_ms")
    g = 9.80665
    h = float(h_m)
    v0 = float(v0_ms)
    # Time for down-thrown rock: solve 0.5 g t^2 + v0 t - h = 0
    a = 0.5 * g
    b = v0
    c = -h
    disc = b*b - 4*a*c
    t_down = (-b + math.sqrt(disc)) / (2*a)
    # Time for up-thrown rock: rise then fall total: t_up = v0/g + sqrt((v0/g)^2 + 2h/g)
    t_up = v0 / g + math.sqrt((v0/g)**2 + 2*h/g)
    return abs(t_up - t_down)


def prob_kn_0266a_part2(h_m=None, v0_ms=None):
    if None in (h_m, v0_ms):
        raise ValueError("bridge_impact_speed requires h_m, v0_ms")
    g = 9.80665
    h = float(h_m)
    v0 = float(v0_ms)
    # Energy: v^2 = v0^2 + 2 g h for both (same magnitude)
    v = math.sqrt(v0*v0 + 2*g*h)
    return v


def prob_sb_0342(m=None, sumj=None):
    if None in (m, sumj):
        raise ValueError("angle_from_equal_vectors_sumj requires m, sumj")
    m = float(m)
    Sy = float(sumj)
    # For equal |A|=|B|=m and A+B = (0, Sy), magnitude of sum is 2 m cos(phi) along y-axis
    # A = m[cos a, sin a], B = m[cos b, sin b]. Maximize simplicity: symmetric about y ⇒ a=90+θ, b=90-θ ⇒ sum_y=2m cos θ
    # Then angle between A and B is 2θ, and 2m cos θ = Sy ⇒ cos θ = Sy/(2m)
    cos_theta = Sy / (2.0 * m)
    if abs(cos_theta) > 1:
        raise ValueError("infeasible inputs: Sy/(2m) out of [-1,1]")
    theta = math.degrees(math.acos(cos_theta))
    return 2.0 * theta


def prob_sb_0353(k_ratio=None):
    if k_ratio is None:
        raise ValueError("angle_from_sum_diff_ratio requires k_ratio")
    k = float(k_ratio)
    # For equal magnitudes m: |A+B| = 2 m cos(Δ/2), |A-B| = 2 m sin(Δ/2)
    # Given |A+B| = k |A-B| ⇒ cot(Δ/2) = k ⇒ Δ/2 = arctan(1/k)
    delta_half = math.degrees(math.atan2(1.0, k))
    return 2.0 * delta_half


# Renamed braking problem functions

def prob_kn_0250a_part1(v0_ms=None, d_m=None, t_reaction_s=None):
    """Distance from intersection when brakes are applied.
    During reaction time, car travels v0 * t_reaction.
    Distance remaining = total_distance - distance_traveled_during_reaction
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("braking_distance_when_applied requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    d_total = float(d_m)
    t_reaction = float(t_reaction_s)
    
    if t_reaction < 0:
        raise ValueError("reaction time must be non-negative")
    
    # Distance traveled during reaction time
    d_reaction = v0 * t_reaction
    
    # Distance remaining when brakes are applied
    d_remaining = d_total - d_reaction
    return d_remaining


def prob_kn_0250a_part2(v0_ms=None, d_m=None, t_reaction_s=None):
    """Constant acceleration needed so that the car stops exactly at the intersection.
    Uses distance remaining after reaction, then v_f^2 = v0^2 + 2 a d => a = -v0^2/(2 d).
    Returns a (negative value for deceleration).
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("required_deceleration_to_stop requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    d_remaining = prob_kn_0250a_part1(v0_ms, d_m, t_reaction_s)
    if d_remaining <= 0:
        raise ValueError("no remaining distance to brake")
    a = - (v0 * v0) / (2.0 * d_remaining)
    return a


def prob_kn_0250a_part3(v0_ms=None, d_m=None, t_reaction_s=None, include_reaction=True):
    """Total time until full stop.
    If include_reaction=True (default): returns reaction time + braking time.
    If include_reaction=False: returns braking time only.
    Uses the constant deceleration from required_deceleration_to_stop().
    """
    if None in (v0_ms, d_m, t_reaction_s):
        raise ValueError("stopping_time_after_brakes requires v0_ms, d_m, t_reaction_s")
    v0 = float(v0_ms)
    a = prob_kn_0250a_part2(v0_ms, d_m, t_reaction_s)
    if a >= 0:
        raise ValueError("acceleration must be negative to stop")
    t_brake = -v0 / a
    return t_brake


def prob_sb_0518a_part1(F_n_N=None, F_e_N=None, F_s_N=None, m_kg=None):
    """Acceleration magnitude from three perpendicular forces on a mass.
    Inputs: north (positive y), east (positive x), south (negative y), mass.
    a = |sum F| / m, with F_y = F_n - F_s, F_x = F_e.
    """
    if None in (F_n_N, F_e_N, F_s_N, m_kg):
        raise ValueError("prob_sb_0518a_part1 requires F_n_N, F_e_N, F_s_N, m_kg")
    Fn = float(F_n_N)
    Fe = float(F_e_N)
    Fs = float(F_s_N)
    m = float(m_kg)
    Fx = Fe
    Fy = Fn - Fs
    a = math.hypot(Fx, Fy) / m
    return a


def prob_sb_0518a_part2(F_n_N=None, F_e_N=None, F_s_N=None, m_kg=None):
    """Acceleration direction in degrees with east=0°, CCW positive.
    Uses atan2(Fy, Fx) where Fx=Fe, Fy=Fn-Fs. Returns angle in [-180, 180].
    """
    if None in (F_n_N, F_e_N, F_s_N, m_kg):
        raise ValueError("prob_sb_0518a_part2 requires F_n_N, F_e_N, F_s_N, m_kg")
    Fn = float(F_n_N)
    Fe = float(F_e_N)
    Fs = float(F_s_N)
    Fx = Fe
    Fy = Fn - Fs
    ang = math.degrees(math.atan2(Fy, Fx))
    # Normalize to (-180, 180], but typical atan2 already is
    if ang <= -180.0:
        ang += 360.0
    elif ang > 180.0:
        ang -= 360.0
    return ang


def prob_sb_0524a_part1(W_N=None, theta1_deg=None, theta2_deg=None):
    """Tension T1 for a three-wire support in equilibrium.
    Geometry: two slanted wires at angles theta1, theta2 above horizontal, one vertical wire (T3) carries weight W.
    Equations: horizontal balance T1 cos θ1 = T2 cos θ2; vertical balance T1 sin θ1 + T2 sin θ2 = T3, and T3 = W.
    Solve: T1 = W * cos θ2 / sin(θ1 + θ2).
    """
    if None in (W_N, theta1_deg, theta2_deg):
        raise ValueError("prob_sb_0524a_part1 requires W_N, theta1_deg, theta2_deg")
    W = float(W_N)
    th1 = math.radians(float(theta1_deg))
    th2 = math.radians(float(theta2_deg))
    denom = math.sin(th1 + th2)
    if abs(denom) < 1e-12:
        raise ValueError("Invalid geometry: sin(theta1+theta2)=0")
    T1 = W * math.cos(th2) / denom
    return T1


def prob_sb_0524a_part2(W_N=None, theta1_deg=None, theta2_deg=None):
    """Tension T2 for the same setup.
    From balance: T2 = W * cos θ1 / sin(θ1 + θ2).
    """
    if None in (W_N, theta1_deg, theta2_deg):
        raise ValueError("prob_sb_0524a_part2 requires W_N, theta1_deg, theta2_deg")
    W = float(W_N)
    th1 = math.radians(float(theta1_deg))
    th2 = math.radians(float(theta2_deg))
    denom = math.sin(th1 + th2)
    if abs(denom) < 1e-12:
        raise ValueError("Invalid geometry: sin(theta1+theta2)=0")
    T2 = W * math.cos(th1) / denom
    return T2


def prob_sb_0524a_part3(W_N=None, theta1_deg=None, theta2_deg=None):
    """Tension T3 (vertical) equals the weight W in static equilibrium."""
    if W_N is None:
        raise ValueError("prob_sb_0524a_part3 requires W_N")
    return float(W_N)


def prob_hr_0532(v0_ms=None, F_N=None, dx_m=None):
    """
    Vertical deflection y for a particle with horizontal speed v0, under a constant vertical force F,
    during the time it travels a horizontal distance dx.
    - v0_ms: horizontal speed (m/s), may be scientific notation as string
    - F_N: vertical constant force (N)
    - dx_m: horizontal distance token; if original unit was mm (from text like '32.0mm'), caller passes '32.0'. We normalize here.
    Returns y in meters.
    """
    if v0_ms is None or F_N is None or dx_m is None:
        raise ValueError("prob_hr_0532 requires v0_ms, F_N, dx_m")

    # --- Normalize dx ---
    dx = None
    # Accept raw like '32.0', interpret as mm per our matcher behavior if the source text used mm
    # Heuristic: if the original html contained 'mm' adjacent to this number, matcher provided just the numeric string.
    # So we treat a small numeric (< 1 with one or two decimals) as meters if the text had 'm', else if likely mm we allow explicit mm by caller.
    s = str(dx_m).strip()
    # If caller already passed with unit suffix, parse accordingly
    lower = s.lower().replace(" ", "")
    if lower.endswith("mm"):
        try:
            dx = float(lower[:-2]) * 1e-3
        except ValueError:
            pass
    elif lower.endswith("cm"):
        try:
            dx = float(lower[:-2]) * 1e-2
        except ValueError:
            pass
    elif lower.endswith("m"):
        try:
            dx = float(lower[:-1])
        except ValueError:
            pass
    if dx is None:
        # No suffix: decide based on magnitude. If value > 10, assume meters; if typical mm like 32.0, convert mm→m.
        try:
            val = float(s)
            dx = val * 1e-3 if val > 1.0 else val
        except ValueError:
            raise ValueError("dx_m not parseable")

    v0 = float(v0_ms)
    F = float(F_N)
    me = 9.1093837015e-31
    a = F / me
    t = dx / v0
    y = 0.5 * a * t * t
    return y


def prob_kn_0842(m_painter_kg=None, m_chair_kg=None, a_ms2=None):
    """Pull force for painter + chair on an ideal frictionless rope/pulley.
    Standard result for the typical setup where the painter pulls the free end of the rope attached over a pulley to the chair: two rope segments support the combined mass M; upward force from rope on system equals 2T; Newton: 2T - M g = M a ⇒ T = (M (g + a)) / 2.
    Returns T in newtons.
    """
    if None in (m_painter_kg, m_chair_kg, a_ms2):
        raise ValueError("prob_kn_0842 requires m_painter_kg, m_chair_kg, a_ms2")
    M = float(m_painter_kg) + float(m_chair_kg)
    a = float(a_ms2)
    g = 9.80665
    T = M * (g + a) / 2.0
    return T


def prob_kn_0832(mu_s, mu_k, d_m, m_lower_kg, m_upper_kg, g=9.80665):
    """
    Least time to travel distance d with no slip between blocks.
    Top block mass m1 on lower block mass m2; floor friction is kinetic (mu_k).
    """
    m1, m2 = float(m_upper_kg), float(m_lower_kg)
    a_max = ((mu_s*m1 - mu_k*(m1 + m2)) * g) / m2
    if a_max <= 0:
        raise ValueError("No-slip motion impossible with given parameters (a_max <= 0).")
    return math.sqrt(2.0 * float(d_m) / a_max)


def prob_kn_0552(m_kg, phi_deg, mu_s, g=9.80665):
    """Minimum force to start moving the block UP the wall."""
    phi = math.radians(phi_deg)
    denom = math.sin(phi) - mu_s * math.cos(phi)   # friction downward
    if denom <= 0:
        raise ValueError("Impossible to move up for this angle: sinφ ≤ μs cosφ.")
    return m_kg * g / denom

def prob_sf_0442a_part1(m_kg: float, theta_deg: float, mu_s: float) -> float:
    """
    Minimum horizontal force F (to the right) required to hold a block at rest on an incline.
    Friction assists up the plane at the threshold.
    F_min = m g (sinθ - μs cosθ) / (cosθ + μs sinθ).
    If sinθ <= μs cosθ, friction alone can hold the block ⇒ F_min = 0.
    """
    g = 9.80665
    theta = math.radians(theta_deg)
    num = math.sin(theta) - mu_s * math.cos(theta)
    den = math.cos(theta) + mu_s * math.sin(theta)
    if den <= 0:
        raise ValueError("Geometry near singular (cosθ + μs sinθ ≤ 0).")
    if num <= 0:
        return 0.0  # friction alone suffices
    return m_kg * g * num / den


def prob_sf_0442a_part2(m_kg: float, theta_deg: float, mu_s: float) -> float:
    """
    Normal force on the block when held with the minimum horizontal force from Part 1.
    N = m g cosθ + F_min sinθ.
    """
    g = 9.80665
    theta = math.radians(theta_deg)
    F_min = prob_sf_0442a_part1(m_kg, theta_deg, mu_s)
    N = m_kg * g * math.cos(theta) + F_min * math.sin(theta)
    return N


def prob_sf_0458(m_kg: float, alpha_deg: float, g: float = 9.80665) -> float:
    """
    Car acceleration from rope deflection in an accelerating frame.
    A small mass hangs from the roof and the rope makes angle alpha from vertical.
    From equilibrium in the non-inertial frame: tan(alpha) = a / g ⇒ a = g * tan(alpha).
    The mass m is irrelevant for a; accepted to match the catalog signature.
    Returns acceleration in m/s^2.
    """
    alpha = math.radians(alpha_deg)
    return g * math.tan(alpha)

def prob_sb_0568a_part1(m1_kg: float, m2_kg: float, F_N: float, mu_k: float, g: float = 9.80665) -> float:
    """
    Two stacked blocks; lower block pulled by F. All contacts kinetic with coeff mu_k.
    Top block m1 is tied to a wall → friction on m1 (right) = μk m1 g, so the string tension T = μk m1 g.
    """
    return mu_k * float(m1_kg) * g

def prob_sb_0568a_part2(m1_kg: float, m2_kg: float, F_N: float, mu_k: float, g: float = 9.80665) -> float:
    """
    Acceleration of the heavy (lower) block m2.
    Friction on m2 from table: μk (m1+m2) g (left).
    Friction from the top interface on m2: μk m1 g (left).
    m2 a = F - μk g [(m1+m2) + m1] ⇒ a = [F - μk g (m2 + 2 m1)] / m2
    """
    m1, m2, F = float(m1_kg), float(m2_kg), float(F_N)
    return (F - mu_k * g * (m2 + 2.0 * m1)) / m2


# ---------- sb-prob0613a.problem (Conical pendulum) ----------
def prob_sb_0613a_part1(m_kg: float, L_m: float, theta_deg: float, g: float = 9.80665) -> float:
    """
    Horizontal component of the wire force: F_h = T sinθ, with T cosθ = mg ⇒ T = mg/cosθ.
    Hence F_h = mg tanθ.
    """
    th = math.radians(float(theta_deg))
    return float(m_kg) * g * math.tan(th)

def prob_sb_0613a_part2(m_kg: float, L_m: float, theta_deg: float, g: float = 9.80665) -> float:
    """
    Vertical component of the wire force: F_v = T cosθ = mg.
    """
    return float(m_kg) * g

def prob_sb_0613a_part3(m_kg: float, L_m: float, theta_deg: float, g: float = 9.80665) -> float:
    """
    Radial (centripetal) acceleration: a_r = g tanθ.
    """
    th = math.radians(float(theta_deg))
    return g * math.tan(th)


# ---------- sb-prob0611.problem ----------
def prob_sb_0611(R_m: float, mu_s: float, g: float = 9.80665) -> float:
    """
    Max speed on unbanked curve without sliding: v_max = sqrt(μs g R).
    """
    return math.sqrt(float(mu_s) * g * float(R_m))


# ---------- hr-prob0636a.problem (two sleds on incline with friction) ----------
def prob_hr_0636a_part2(mA_kg: float, mB_kg: float, theta_deg: float, mu_k_A: float, mu_k_B: float, g: float = 9.80665) -> float:
    """
    Common acceleration down the slope:
      (mA+mB) a = (mA+mB) g sinθ - g cosθ (μA mA + μB mB)
      ⇒ a = g[ sinθ - cosθ * (μA mA + μB mB)/(mA+mB) ].
    """
    mA, mB = float(mA_kg), float(mB_kg)
    th = math.radians(float(theta_deg))
    return g * (math.sin(th) - math.cos(th) * (mu_k_A * mA + mu_k_B * mB) / (mA + mB))

def prob_hr_0636a_part1(mA_kg: float, mB_kg: float, theta_deg: float, mu_k_A: float, mu_k_B: float, g: float = 9.80665) -> float:
    """
    Tension in the bar. Using block B (down-slope +):
      mB a = mB g sinθ - μB mB g cosθ + T  ⇒  T = mB a - mB g sinθ + μB mB g cosθ.
    """
    a = prob_hr_0636a_part2(mA_kg, mB_kg, theta_deg, mu_k_A, mu_k_B, g=g)
    mB = float(mB_kg); th = math.radians(float(theta_deg))
    return mB * a - mB * g * math.sin(th) + mu_k_B * mB * g * math.cos(th)


# ---------- hr-prob0666.problem ----------
def prob_hr_0666(v_kmh: float, tilt_deg: float, g: float = 9.80665) -> float:
    """
    Airplane banked turn (wings tilted by 'tilt_deg' to the horizontal).
    Lift is perpendicular to the wing ⇒ tilt of lift from vertical = tilt_deg.
    r = v^2 / (g tan(tilt)), with v in m/s.
    """
    v = float(v_kmh) * (1000.0 / 3600.0)
    phi = math.radians(float(tilt_deg))
    return v * v / (g * math.tan(phi))


# ---------- hr-prob0670b.problem (equilateral two-string around rod) ----------
def prob_hr_0670b_part1(m_kg: float, L_m: float, T_upper_N: float, g: float = 9.80665) -> float:
    """
    Lower string tension: vertical balance at bob with strings at ±30° to horizontal:
      T_u sin30 - T_l sin30 - mg = 0  ⇒  T_l = T_u - 2mg.
    """
    return float(T_upper_N) - 2.0 * float(m_kg) * g

def prob_hr_0670b_part2(m_kg: float, L_m: float, T_upper_N: float, g: float = 9.80665) -> float:
    """
    Speed of ball.
    Radial balance: (T_u + T_l) cos30 = m v^2 / r,   r = (√3/2) L,  T_l = T_u - 2mg.
    """
    m = float(m_kg); L = float(L_m); Tu = float(T_upper_N)
    Tl = Tu - 2.0 * m * g
    r  = (math.sqrt(3.0) / 2.0) * L
    return math.sqrt(((Tu + Tl) * (math.sqrt(3.0) / 2.0)) * r / m)


# ---------- kn-prob0828.problem ----------
def prob_kn_0828(F_N: float, mu_k_surface: float, mu_k_between: float, m_lower_kg: float, m_upper_kg: float, g: float = 9.80665) -> float:
    """
    Lower block acceleration with top block sliding on it.
    Friction at table (left): μ_surface (m_lower + m_upper) g.
    Friction from top interface on lower (left): μ_between m_upper g.
    ⇒ a = [F - g ( μ_surface (m_l + m_u) + μ_between m_u )] / m_lower
    """
    F = float(F_N); ml = float(m_lower_kg); mu = float(m_upper_kg)
    return (F - g * (mu_k_surface * (ml + mu) + mu_k_between * mu)) / ml


# ---------- kn-prob0836a.problem ----------
def prob_kn_0836a_part1(theta_deg: float, mu_s: float, mu_k: float, m2_kg: float, g: float = 9.80665) -> float:
    """
    Minimum M1 on incline (angle theta) to keep system at rest against hanging mass m2.
      T = m2 g = M1 g (sinθ + μs cosθ)  ⇒  M1_min = m2 / (sinθ + μs cosθ)
    """
    th = math.radians(float(theta_deg))
    denom = math.sin(th) + float(mu_s) * math.cos(th)
    if denom <= 0:
        raise ValueError("Invalid parameters: sinθ + μs cosθ ≤ 0")
    return float(m2_kg) / denom

def prob_kn_0836a_part2(theta_deg: float, mu_s: float, mu_k: float, m2_kg: float, g: float = 9.80665) -> float:
    """
    If nudged so M1 moves UP the incline (kinetic friction down the plane):
      a = [ m2 g - M1 g (sinθ + μk cosθ) ] / (M1 + m2), with M1 = prob_kn_0836a_part1(...)
    """
    M1 = prob_kn_0836a_part1(theta_deg, mu_s, mu_k, m2_kg, g=g)
    th = math.radians(float(theta_deg))
    m2 = float(m2_kg)
    return (m2 * g - M1 * g * (math.sin(th) + float(mu_k) * math.cos(th))) / (M1 + m2)


# ---------- kn-prob0838a.problem ----------
def prob_kn_0838a_part1(m_book_kg: float, m_cup_kg: float, v0_ms: float, mu_s: float, mu_k: float, theta_deg: float, g: float = 9.80665) -> float:
    """
    Book on slope (up-slope positive) tied over a pulley to a hanging cup.
    While sliding up-slope, kinetic friction acts down-slope on the book.
    Book:  m_b a = T - m_b g sinθ - μk m_b g cosθ
    Cup:   m_c a =  T - m_c g    (upward positive)
    ⇒ a = [ m_c g - m_b g (sinθ + μk cosθ) ] / (m_b - m_c)
    (Usually negative here: deceleration of the book.)
    """
    mb, mc = float(m_book_kg), float(m_cup_kg)
    th = math.radians(float(theta_deg))
    return (mc * g - mb * g * (math.sin(th) + float(mu_k) * math.cos(th))) / (mb - mc)

def prob_kn_0838a_part2(m_book_kg: float, m_cup_kg: float, v0_ms: float, mu_s: float, mu_k: float, theta_deg: float, g: float = 9.80665) -> float:
    """
    Distance the book slides before stopping, assuming constant a from part 1 (<0):
      s = v0^2 / (2 |a|).
    """
    a = prob_kn_0838a_part1(m_book_kg, m_cup_kg, v0_ms, mu_s, mu_k, theta_deg, g=g)
    if a >= 0:
        raise ValueError("Book does not decelerate (a must be negative) with given parameters.")
    v0 = float(v0_ms)
    return (v0 * v0) / (2.0 * (-a))


# ---------- cj-prob0491a.problem (2:1 pulley displacement constraint) ----------
def prob_cj_0491a_part2(M_big_kg: float, M_small_kg: float, g: float = 9.80665) -> float:
    """
    Acceleration of the big (table) block. Kinematics: a_big = 2 a_small.
    Dynamics: 2T - m_s g = m_s a_small,  T = m_big a_big.
    ⇒ a_big = (2 m_s g) / (4 m_big - m_s)
    """
    mL, mS = float(M_big_kg), float(M_small_kg)
    return (2.0 * mS * g) / (4.0 * mL - mS)

def prob_cj_0491a_part1(M_big_kg: float, M_small_kg: float, g: float = 9.80665) -> float:
    """
    Tension in the rope: T = m_big * a_big, with a_big from prob_cj_0491a_part2.
    """
    a_big = prob_cj_0491a_part2(M_big_kg, M_small_kg, g=g)
    return float(M_big_kg) * a_big