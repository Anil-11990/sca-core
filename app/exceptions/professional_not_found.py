"""
Raised when a Professional cannot be found.
"""


class ProfessionalNotFoundException(Exception):
    """
    Raised when a Professional does not exist.
    """

    def __init__(
        self,
        professional_id: str,
    ):

        super().__init__(
            f"Professional '{professional_id}' was not found."
        )