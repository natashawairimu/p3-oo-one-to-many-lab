class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type. Must be one of: {', '.join(Pet.PET_TYPES)}")

        from owner import Owner  # Delayed import to prevent circular dependency
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
