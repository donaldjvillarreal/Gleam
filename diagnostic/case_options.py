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

goal_frequencies = [('%i times a week' % i, i) for i in range(1, 8)]
