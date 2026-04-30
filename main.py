from Exercise import (
    display_main_menu,
    get_user_input,
    calc_average,
    find_min_max,
    sort_temperature,
    calc_median_temperature,
)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatnumbers = get_user_input()
    calc_average(floatnumbers)
    find_min_max(floatnumbers)
    sort_temperature(floatnumbers)
    calc_median_temperature(floatnumbers)


if __name__ == "__main__":
    main()


 