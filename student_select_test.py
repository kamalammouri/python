from select_student import select_student_ok
if __name__ == "__main__":

    assert select_student_ok(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        20
    ) == {
        "Accepted": [["Hattie Schleusner", 67], ["Kermit Wade", 27]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5]]
    }

    assert select_student_ok(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        50,
    ) == {
        "Accepted": [["Hattie Schleusner", 67]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5], ["Kermit Wade", 27]]
    }