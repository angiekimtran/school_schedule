from school_schedule.student import Student

def create_test_student():    
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    return quinn


def test_instantiate_valid_student():
    quinn = create_test_student()

    assert quinn.name == "Quinn"
    assert len(quinn.classes) == 6
    assert quinn.grade == "junior"
    assert quinn.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
    
def test_add_class():
    quinn = create_test_student()

    quinn.add_class("Art")

    assert "Art" in quinn.classes
    assert len(quinn.classes) == 7

def test_get_num_classes():
    quinn = create_test_student()
    
    assert len(quinn.classes) == quinn.get_num_classes()

def test_summary():
    quinn = create_test_student()

    assert quinn.summary() == "Quinn is a junior. Quinn takes 6 classes, which are Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"