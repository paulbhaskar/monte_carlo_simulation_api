import time
from celery import shared_task
from datetime import datetime
from pytz import timezone

from monte_carlo_simulation.models import Trial
from monte_carlo_simulation.poker.texas_holdem import *
from config.utils.log import Log as log
from config.constants import TIME_ZONE, TASK_BATCH_SIZE


# Please name Celery tasks in uppercase

@shared_task(bind=True, name='POKER_BAD_BEAT')
def poker_bad_beat(self, num_of_players):
    """Montecarlo simulations of quads or better getting beat by a better hand when both hole cards play

    Args:
        db_model (django.db.models.Model): Name of Model class
        ro
    """
    start = time.time()
    trials = TASK_BATCH_SIZE
    tz = timezone(TIME_ZONE)
    log.debug(
        f"Task {self.request.id} started at {datetime.now(tz)} with batch size {trials}")
    for _trial in range(trials):
        game = TexasHoldem()
        trial = Trial()

        community_cards = game.community_cards
        trial.community_cards = str(community_cards)
        player_cards = []
        hole_cards = []
        for index in range(num_of_players):
            player_hole_cards = game.deal(2)
            hole_cards.append(player_hole_cards)
            player_card = TexasHoldem.player_cards(
                community_cards, player_hole_cards)
            best_hand = TexasHoldem.determine_hand(player_card)[1]
            best_five_cards = TexasHoldem.calculate_five_cards_used(
                best_hand, community_cards, player_hole_cards, 3, scores={})[0]
            player_cards.append(player_card)

            cards = {}
            cards['hole_cards'] = str(player_hole_cards)
            cards['best_hand'] = str(best_hand)
            cards['best_five_cards'] = str(best_five_cards)
            setattr(trial, "player_" + str(index+1), cards)

        trial_rankings = TexasHoldem.player_hand_rankings(player_cards)
        filtered_trial_rankings = dict(
            (key, value) for key, value in trial_rankings.items() if value >= 8)
        if len(filtered_trial_rankings) >= 2:
            bad_beat_count = 0
            keys = []
            for key, value in filtered_trial_rankings.items():
                if TexasHoldem.check_if_both_hole_cards_used(community_cards, hole_cards[key]):
                    bad_beat_count += 1
                    keys.append(key)
            if bad_beat_count >= 2:
                trial.success = True

        trial.save()

    log.debug(
        f"Task {self.request.id} completed at {datetime.now(tz)} Duration of task was {time.time() - start} seconds")
