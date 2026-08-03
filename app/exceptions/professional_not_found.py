"""
Professional Not Found Exception.

Raised when a Professional
cannot be found in the system.
"""


class ProfessionalNotFoundException(Exception):
    """
    Domain/Application exception.

    Used when searching for a Professional
    that does not exist.
    """


    def __init__(
        self,
        professional_id,
    ):

        self.professional_id = professional_id

        super().__init__(
            f"Professional with id {professional_id} was not found."
        )