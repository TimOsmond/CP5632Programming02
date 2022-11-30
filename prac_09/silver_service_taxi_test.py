"""
Test silver service taxi class.
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi class."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
