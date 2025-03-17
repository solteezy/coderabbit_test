-- Create the lightbulbs table
CREATE TABLE lightbulbs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(50) NOT NULL,
    efficiency VARCHAR(20) NOT NULL,
    lifespan_hours INTEGER NOT NULL,
    initial_cost DECIMAL(10,2) NOT NULL,
    long_term_cost DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO lightbulbs (type, efficiency, lifespan_hours, initial_cost, long_term_cost, description)
VALUES 
    ('LED', 'High', 50000, 15.99, 45.99, 'Energy-efficient LED bulb with long lifespan'),
    ('Incandescent', 'Low', 1200, 2.99, 120.99, 'Traditional incandescent lightbulb'),
    ('CFL', 'Medium', 8000, 8.99, 75.99, 'Compact Fluorescent Lamp - An energy-efficient alternative to incandescent bulbs'),
    ('Smart LED', 'High', 50000, 29.99, 59.99, 'WiFi-enabled LED bulb with smart features'),
    ('Halogen', 'Medium', 2000, 5.99, 90.99, 'Halogen lightbulb with bright white light');

-- Sample Queries:

-- 1. Basic SELECT query to show all lightbulbs
SELECT * FROM lightbulbs;

-- 2. Find the most efficient lightbulbs
SELECT type, efficiency, lifespan_hours
FROM lightbulbs
WHERE efficiency = 'High'
ORDER BY lifespan_hours DESC;

-- 3. Calculate cost savings over 5 years (assuming 4 hours daily usage)
SELECT 
    type,
    lifespan_hours,
    (lifespan_hours / (4 * 365 * 5)) as bulbs_needed,
    (bulbs_needed * initial_cost) as total_cost
FROM lightbulbs
ORDER BY total_cost;

-- 4. Find lightbulbs with lifespan greater than average
SELECT type, lifespan_hours
FROM lightbulbs
WHERE lifespan_hours > (SELECT AVG(lifespan_hours) FROM lightbulbs)
ORDER BY lifespan_hours DESC;

-- Aggregated Queries:

-- 1. Calculate average lifespan and cost by efficiency level
SELECT 
    efficiency,
    AVG(lifespan_hours) as avg_lifespan,
    AVG(initial_cost) as avg_initial_cost,
    AVG(long_term_cost) as avg_long_term_cost
FROM lightbulbs
GROUP BY efficiency
ORDER BY avg_lifespan DESC;

-- 2. Count of lightbulbs by efficiency level
SELECT 
    efficiency,
    COUNT(*) as count,
    ROUND(AVG(lifespan_hours), 0) as avg_lifespan
FROM lightbulbs
GROUP BY efficiency;

-- 3. Cost analysis by type
SELECT 
    type,
    SUM(initial_cost) as total_initial_cost,
    SUM(long_term_cost) as total_long_term_cost,
    (SUM(long_term_cost) - SUM(initial_cost)) as total_savings
FROM lightbulbs
GROUP BY type
ORDER BY total_savings DESC;

-- 4. Efficiency vs Cost Analysis
SELECT 
    efficiency,
    COUNT(*) as count,
    MIN(initial_cost) as min_initial_cost,
    MAX(initial_cost) as max_initial_cost,
    AVG(initial_cost) as avg_initial_cost
FROM lightbulbs
GROUP BY efficiency
ORDER BY efficiency; 