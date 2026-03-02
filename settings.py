from os import environ

SESSION_CONFIGS = [
    dict(
        name="unpopular_norm_4",
        display_name="test_n4",
        num_demo_participants=200,
        group_size=4,
        network_condition="test_n4",
        app_sequence=[ "arrive", "unpop", "survey", "reward"],
        completionlink='https://app.prolific.com/submissions/complete?cc=CGMXM1XJ',
        completionlink_full='https://app.prolific.com/submissions/complete?cc=ZZZZ',
        completionlink_no_invite='https://app.prolific.com/submissions/complete?cc=XXXX',
        use_browser_bots=False,
    ),

    dict(
        name="unpopular_norm_10",
        display_name="test_n10",
        num_demo_participants=200,
        group_size=10,
        network_condition="test_n10",
        app_sequence=[ "arrive", "unpop"],
        completionlink='https://app.prolific.com/submissions/complete?cc=CGMXM1XJ',
        completionlink_full='https://app.prolific.com/submissions/complete?cc=ZZZZ',
        completionlink_no_invite='https://app.prolific.com/submissions/complete?cc=XXXX',
        use_browser_bots=False,
    ),
]

# set some central parameters to be used across apps:
title = 'The Fashion Dilemma'
majority_role = 'Red'
minority_role = 'Blue'
p_minority = 0.1 # !!this needs to correspond to the proportion of minorities in the network configuration!!
num_rounds = 8 #set back to 30!

# including also the incentive structure
s = 15
e = 10
z = 50
w = 40
lambda1 = 4.3
lambda2 = 1.8

# and payment variables (base pay; conversion rates; etc.)
base_payment = 2.5 #base pay of 2.50 (for estimated 25 min.)
max_payment = 7.5 #max of 7.50
points_per_euro_majority = 200 #conversion (assuming 30 rounds!!)
points_per_euro_minority = 40

# I want to test the whole infrastructure (entering from prolific, consenting, group formation, etc.);
testing = False
# so add some 'disclaimers' to the instructions and consent form etc. ("this is just a test"), conditional on this parameter

#configure a room
ROOMS = [
    dict(
        name='1',
        display_name='Network #1: heterogenous (central fanatics)',
        #participant_label_file='_rooms/fashion_dilemma.txt',
        #use_secure_urls=True,
    ),
    dict(
        name='2',
        display_name='Network #2: homogenous (random)',
        #participant_label_file='_rooms/fashion_dilemma.txt',
        #use_secure_urls=True,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1/30,
    participation_fee=3.00,
    doc="",
)

PARTICIPANT_FIELDS = [ "bonus", "consent", "is_dropout", "role", 'has_dropped_out', 'too_many_inactive_in_group','node', 'adj_matrix', 'role_vector', 'exit_early', 'failed_checks']
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = True
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")
DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = "secret"