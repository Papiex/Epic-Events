from enum import Enum


class CustomerType(Enum):
    """Enum existing or potential customer"""

    POTENTIAL = "Potential customer"
    EXISTING = "Existing customer"
