from typing import List


class Solution:
    """
        Count the rank of vote for each candidate.
        Sort all teams according to the ranking system.
    """

    def rankTeams(self, votes: List[str]) -> str:
        records = {ch: [0] * len(votes[0]) for ch in votes[0]}
        for vote in votes:
            for i, ch in enumerate(vote):
                records[ch][i] -= 1
        return ''.join(sorted(votes[0], key=lambda v: records[v] + [v]))
