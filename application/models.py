from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class ResultsData(models.Model):
    atp = models.IntegerField(default=0,
                              help_text=_lazy("Tournament number (men)"))
    wta = models.IntegerField(default=0,
                              help_text=_lazy("Tournament number (Women)"))
    location = models.CharField(max_length=100)
    tournament = models.TextField()
    date = models.DateTimeField()
    series = models.CharField(max_length=100)
    tier = models.CharField(max_length=100,
                            help_text=_lazy("Tier (tournament ranking) of WTA tennis series"))
    court = models.CharField(max_length=150)
    surface = models.CharField(max_length=50,
                               help_text=_lazy("Type of surface (clay, hard, carpet or grass)"))
    round = models.CharField(max_length=150,
                             help_text=_lazy("Round of match"))
    best_of = models.IntegerField(default=0,
                                  help_text=_lazy("Maximum number of sets playable in match"))
    winner = models.CharField(max_length=100,
                              help_text=_lazy("Match winner"))
    loser = models.CharField(max_length=100)
    wrank = models.PositiveIntegerField(default=0,
                                        help_text=_lazy("ATP Entry ranking of the match winner as of the "
                                                        "start of the tournament"))
    lrank = models.PositiveIntegerField(default=0)
    wPts = models.PositiveIntegerField(default=0,
                                       help_text=_lazy("ATP Entry points of the match winner as of the "
                                                       "start of the tournament"))
    lpts = models.PositiveIntegerField(default=0)
    w1 = models.IntegerField(null=True,
                             blank=True,
                             help_text=_lazy("Number of games won in 1st set by match winner"))
    l1 = models.IntegerField(null=True, blank=True)
    w2 = models.IntegerField(null=True, blank=True)
    l2 = models.IntegerField(null=True, blank=True)
    w3 = models.IntegerField(null=True, blank=True)
    l3 = models.IntegerField(null=True, blank=True)
    w4 = models.IntegerField(null=True, blank=True)
    l4 = models.IntegerField(null=True, blank=True)
    w5 = models.IntegerField(null=True, blank=True)
    l5 = models.IntegerField(null=True, blank=True)
    wsets = models.IntegerField(null=True, blank=True,
                                help_text=_lazy("Number of sets won by match winner"))
    lsets = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=150)
    b365w = models.FloatField(null=True,
                              help_text=_lazy("Bet365 odds of match winner"))
    b365l = models.FloatField(null=True)
    exw = models.FloatField(null=True,
                            help_text=_lazy("Expekt  odds of match winner"))
    exl = models.FloatField(null=True)
    lbw = models.FloatField(null=True,
                            help_text=_lazy("Ladbrokes odds of match winner"))
    lbl = models.FloatField(null=True)
    psw = models.FloatField(null=True,
                            help_text=_lazy("Pinnacles odds of match winner"))
    psl = models.FloatField(null=True)
    sjw = models.FloatField(null=True,
                            help_text=_lazy("Stan James odds of match winner"))
    sjl = models.FloatField(null=True)
    maxw = models.FloatField(null=True,
                             help_text=_lazy("Maximum odds of match winner (as shown by Oddsportal.com)"))
    maxl = models.FloatField(null=True)
    avgw = models.FloatField(null=True,
                             help_text=_lazy("Average odds of match winner (as shown by Oddsportal.com)"))
    avgl = models.FloatField(null=True)

    class Meta:
        verbose_name = "Results data"
        verbose_name_plural = "Results data"

    def remove_all_object(self):
        self.objects.all().delete()

    def __str__(self):
        return 'Id: {0}'.format(str(self.pk))


def add_data_from_xls(cases):
    count = 0
    for row in cases:
        d, new = ResultsData.objects.get_or_create(**row)
        print(d)
    # if not new:
    #     print("Entry already in the DB")
    #     print(d)
    #     continue
    # count += 1
    return
