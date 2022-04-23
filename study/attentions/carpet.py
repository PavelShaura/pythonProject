def carpet(w, h):
    one_line = "█" + "░" * (w - 2) + "█"
    two_line = "█" + "░" + "█" * (w - 4) + "░" + "█"

    print(one_line)
    for i in range(h - 2):
        if w > 2:
            print(two_line)
        else:
            print(one_line)
    print(one_line)


carpet(25, 6)
