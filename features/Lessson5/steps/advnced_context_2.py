from behave import given, when, then


@given('Init new counter')
def step_impl(context):
    context.counter = 0

@when('Push {button_color} button')
def step_impl(context,button_color):
    if button_color == "red":
        context.counter += 1
    elif button_color == "blue":
        context.counter -= 1

@when('Do it again')
def step_impl(context):
    button_color = "red"
    context.execute_steps(f'when Push {button_color} button')

@when('One more time')
def step_impl(context):
    context.execute_steps(f'when Do it again')

@then('Expected counter equal {counter_value}')
def step_impl(context, counter_value):
    print(context.counter)
    assert context.counter == int(counter_value), 'Doesn\'t work... Why?'