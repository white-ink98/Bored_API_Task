import argparse
from API_Wrapper import BoredAPIWrapper
from Database_Class import ActivityDatabase


def main():
    parser = argparse.ArgumentParser(description="Random activity generator")
    parser.add_argument("command", choices=["new", "list"], help="Command to execute")
    parser.add_argument("--type", help="Filter by activity type")
    parser.add_argument("--participants", type=int, help="Number of participants")
    parser.add_argument("--price_min", type=float, help="Minimum price")
    parser.add_argument("--price_max", type=float, help="Maximum price")
    parser.add_argument("--accessibility_min", type=float, help="Minimum accessibility")
    parser.add_argument("--accessibility_max", type=float, help="Maximum accessibility")

    args = parser.parse_args()

    if args.command == "new":
        activity_params = {
            "type": args.type,
            "participants": args.participants,
            "price": args.price_min,
            "price_max": args.price_max,
            "accessibility": args.accessibility_min,
            "accessibility_max": args.accessibility_max,
        }
        activity = BoredAPIWrapper().get_random_activity(activity_params)
        print("Random Activity:", activity["activity"])
        db = ActivityDatabase("activities.db")
        db.save_activity(activity)
    elif args.command == "list":
        db = ActivityDatabase("activities.db")
        latest_activities = db.get_latest_activities()
        print("Latest Activities:")
        for activity in latest_activities:
            print(activity)


if __name__ == "__main__":
    main()
