from graphql_jwt.decorators import user_passes_test, exceptions

# permissions: only user with verified email
email_verified = user_passes_test(lambda u: u.email_verified)