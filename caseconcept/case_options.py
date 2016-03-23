# coding=utf-8
FREQUENCY_CHOICES = ((0, 'Every day'),
                     (1, 'Once a week'),
                     (2, 'Once a month'),
                     (3, 'Every few months'),
                     )

SEVERITY_CHOICES = ((0, 'Very Minor'),
                    (1, 'Minor'),
                    (2, 'Moderate'),
                    (3, 'Serious'),
                    (4, 'Very Serious'),
                    )

goal_frequencies = [('%i times a week' % i, i) for i in range(1, 5)]

DEFAULT_PROBLEMS = [
    'Family',
    'Work',
    'Friendships',
    'Romantic Relationships',
    'Self-Esteem',
    'Recreational Activites',
    'School'
]

weekday_time_verbose = {1: 'Sunday',
                        2: 'Monday',
                        3: 'Tuesday',
                        4: 'Wednesday',
                        5: 'Thursday',
                        6: 'Friday',
                        7: 'Saturday'}
