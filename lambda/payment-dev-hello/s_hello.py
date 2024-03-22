import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='igorzw',
    application_name='payment',
    app_uid='fKGSsdT6VMgDxq2c7x',
    org_uid='8685d131-09da-4403-b8cb-3ebe6237c586',
    deployment_uid='63a8a7f1-256f-405f-ad9d-7c8d1334ce5b',
    service_name='payment',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='7.2.3',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'payment-dev-hello', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('Payment.handler')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
