INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES
  ('Andrew Brown', 'andrewbrown' , 'testemail@gmail.com', 'MOCK'),
  ('Andrew Bayko', 'bayko' , 'email2@gmail.com', 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = handle LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )