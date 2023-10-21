# Computer Vision Workout

This project uses computer vision to track your reps for curls, push-ups, and squats. This can help ensure that you reach the appropriate depth for each rep, and count your reps so that you can focus on your workout.  

You can view the source code here:
- [main.py](/main.py)

## Changing Workout

In order to change the workout, you must change hte `workout` variable:

On line 11 of [main.py](/main.py), you will see the following code:
```python
workout = "push-up"  # "curl", "squat"
```
Change this string to any of the following variables to change the workout:

- `"push-up"`
- `"curl"`
- `"squat"`

> When running this script, make sure to have the right side of your body face the camera for proper measurement.
