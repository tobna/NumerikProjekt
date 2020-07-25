class RewardI:
    def call(self, state_prev, state_post, phase_prev, player):
        raise NotImplementedError()

    def __call__(self, state_prev, state_post, phase_prev, player):
        return self.call(state_prev, state_post, phase_prev, player)


class SimpleReward(RewardI):
    def __init__(self, take_factor=1.0, penalty=0.0, win_reward=100.0):
        self.pen = penalty
        self.take_factor = take_factor
        self.win = win_reward

    def call(self, state_prev, state_post, phase_prev, player):
        if state_post.is_terminal(phase_prev, player):
            if len(state_post.get_player_pos(player)) >= 3 and len(state_post.legal_moves(phase_prev, player)) > 0:
                return self.win
            return -self.win
        diff_own_pieces = len(state_prev.get_player_pos(player)) - len(state_post.get_player_pos(player))
        diff_enemy_pieces = len(state_prev.get_player_pos(1-player)) - len(state_post.get_player_pos(1-player))
        return (diff_enemy_pieces-diff_own_pieces) * self.take_factor - self.pen