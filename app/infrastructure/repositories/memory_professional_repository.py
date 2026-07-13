class MemoryProfessionalRepository:
    """
    In-memory repository for storing Professionals.

    This implementation is used during development and testing.
    Later it will be replaced with PostgreSQL.
    """

    def __init__(self):
        # Dictionary keyed by Professional ID.
        self._professionals = {}

    def save(self, professional):
        """
        Save or update a Professional.
        """
        self._professionals[professional.id] = professional

    def get_by_id(self, professional_id):
        """
        Retrieve a Professional by its unique ID.

        Returns:
            Professional if found, otherwise None.
        """
        return self._professionals.get(professional_id)