import functions_4_cl

if __name__ == "__main__":
    while True:
        functions_4_cl.clear_screen()
        current_time = functions_4_cl.get_current_time()
        functions_4_cl.print_digits(current_time)
        functions_4_cl.sleep(0.2)
