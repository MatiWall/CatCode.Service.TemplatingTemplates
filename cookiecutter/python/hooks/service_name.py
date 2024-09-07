from cookiecutter.exceptions import FailedHookException


def create_service_name(context):
    try:
        # Access the context dictionary
        system = context.get('system', '')
        application = context.get('application', '')
        deployable_unit = context.get('deployable_unit', '')

        # Combine inputs into a new context variable
        context['service_name'] = f"{system}.{application}.{deployable_unit}"

    except Exception as e:
        raise FailedHookException(f"Failed to combine inputs: {e}")

    return context

# Run the function
create_service_name(context)
