-- Can I define a function?
ADD function ADD_REAL(x real, y real)
    RETURNS real AS $$
    BEGIN
        RETURN x + y;
    END; $$
    LANGUAGE plpgsql; -- PostgreSQL Tagline, I guess...?
-- * Answer: Yes!