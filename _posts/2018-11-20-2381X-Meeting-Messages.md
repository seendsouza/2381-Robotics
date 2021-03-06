---
title: "2381X Meeting Messages"
author: "Anthony Luo"
date: 2018-11-20 -0500
---
This log comes after a few meetings, because we didn’t do much work, we spent most of the time on driver practice, and the work done accumulatively across these meetings is equal to one regular meeting, so we will summarize.
# Intake
After running the robot for a little bit, we realized that bars on the intake would not hold up to the rigors of competition - especially not to other robots continually ramming into us. We changed the intake to be 2-wide c-channel, screwed on using nylocks. They didn’t reach all the way, so we used the bars and extended the c-channels reach. Highly unlikely that any robot is going to hit us that far in, and the bar is supported very well. The c-channels themselves were losing position when we hit balls near the edge of the field, and we couldn’t brace to the other inside drive c-channel, so we came up with an innovative solution of using a hard stop to the top of the c-chanel. A small keps nut screwed down stops the c-channel against the other one. 
What this does is prevent the intake from swinging around, and is strong enough to sustain multiple matches.
# Driver Preferences
During the first driver meeting, all we did was experiment with many different control schemes. Here’s a list:
1. Arcade
2. Tank
3. Split arcade
Here’s how each control system works, arcade maps left and right to one single joystick, forward/back mapped to one axis and turning mapped to another axis. The combination of this means that the motion of the entire robot can be controlled from one joystick. That’s the advantage. The disadvantage is that it’s very difficult to control the robot finely, because you can’t make single sided adjustments very easily, and only doing a point turn or driving straight is more difficult (without deadzones in code). The control system is also limited to certain speeds while turning, and not always the max speed. Tank maps each vertical axis of a joystick to each side of the drivetrain. What we have to do to move forward is push forward on both sticks, and to turn we run one side less than the other. This allows us control on the individual sides of each drive. The disadvantage to tank is that both sides need to be controlled together. The last control sccheme is split arcade, which takes arcade and splits it up, so driving forward and backwards is controlled on one axis, and turrning clockwise or counter-clockwise is controlled on another. This means that forward/backwards is independent for turning. This is kind of like arcade where the entire robot is moved together coherently, but is also similar to tank as you need both sticks working to drive. All three different control systems can be driven to an incredibly good standard, and there are great examples for each control scheme. Many teams that have been division finalists at worlds have used these different controls, and at the end of the day any good driver should be able to use any control system and become highly effective with it. 
In the end, we decided to use split arcade, both the main driver and backup driver decided that running split arcade would be the best option. Tank was difficult because it’s difficult to point turn nicely, adjusting for flags using tank is incredibly ifficult because you need a fine level of control to be able to back up, drive forward, and have a good angle during the entire time. Tank is too easy to mess up the angle, and wasn’t as intuitive. Tank also usually meant that we weren’t driving our robot to full potential because we had to think of what each individual side was doing and match them for a good combination of forward speed and turning. Arcade suffers from many of the same problems as tank, going around the field is easier with arcade, but because of the mapping left/right turning while driving backwards is pretty confusing. Split arcade presented us with the best option because it offered a good combination of isolation in terms of the controls, and at the same time coherence between the two sides of the robot that allow us to have smooth driving - smooth is fast. Split arcade removed the ambiguity on what a turn would look like, we can hold a forward speed and turn to adjust accordingly - this is more difficult on other controls. Once we got used to split arcade, it was pretty hard to go back to anything else. 
Our driver also decided to put flywheel and intake modulation on the shoulder buttons because we found them a lot easier to access, and left them as “holds” because that made the most sense. We left descoring on face buttons because we use it less, and are still able to go forward when descoring - perfect if we line up right. 
After a little bit of trial and error, we decided on a few additions to normal driver code. Normal driver code for drive would map joystick values directly to motor values, which is ok, but due to the nature of our robot, the turning speed is much faster, and thus we have to scale the turning. We also have to adjust the turning so that at low speeds, we are able to have enough power to turn smoothly, and at top speeds be able to limit our turning so we don’t wash out. This is our dirver code
As you can see, the horizontal stick is multiplied by a factor, which is taken from the root function sqrt(x). This means that we have a little bit of a ramp up on our turning, and keeps it consistent and controllable for our driver. 
Our flywheel also has a ramp-up and ramp-down sequence. We realized that spinning up the flywheel using motor=127 (the biggest pwm signal possible), is not a great idea because it’s not putting is in the middle of the power/torque curves. By slowly ramping up the flywheel, we are able to stay in the most powerful state of the motor, which actually translates into a faster spinup time. We have a ramp down which allows us to help save the motors a litlle bit, and also save the gears a litlle bit. It slows down a little bit faster than friction at low speed, and a little bit slower than friction at high speed. This means that at high speed we don’t run a risk of the momentum/intertia from the flywheel destroying our gears - especially the 12 tooth pinion gear. At low speeds, this matters less because the gear is better able to handle it. 
Everything else is fairly simple
# Autonomous
As we are mostly a flag robot, our autonomous routines are predominatly flag oriented. There are two different autonomous paths that we use - one class is the “standalone”, which means that our autonomous run is able to run without collaboration with another robot. The second class is “cooperative”. This is probably going to be used later on, allowing us to gain more points in autonomous. All of our autonomous programs for one side can be mirrored onto the other. I’ll start by describing our front autonomous paths. 
# Front Auton path #1
* start pointed towards flags. 
* Drive forward and hit middle flag, toggle low flag.
* Drive back
* Point turn
* Drive towards ball under cap
* Pick - up ball
* Drive back
* Point turn
* Score high flag
* Drive back
* Point turn
* Drive forward towards middle post
* Point turn
* Toggle low flag
The reason we have this auton is because we aren’t sure whether or not picking up a ball will cause our flywheel to jam (in case the ball feeds too far up). By doing this, we’re able to eliminate the uncertainty, this is a very certain auton, that will definitely gain us a few points. Our scoring distance for the flywheel is also designed so that we can hit the top flag from the starting til, meaning that we have a good shot for the high flag after picking up the ball.
There is a variation upon this auton where we start pointed towards the middle/center. Then, we would just point turn 90 degrees before starting. This allows us to confuse the opponents, especially because we have multiple autonomous starting in the same direction.
# Front Auton path #2
* start pointed towards ball
* Drive forward
* Pick-up ball
* Drive backwards
* Point turn
* High flag
* Drive forward
* Mid flag
* Drive forward into low flag.
This auton is a “riskier” version of the previous auton. This one looks “cooler”, and involves less back and forth. This means that we’re able to stay out of our partners way, for example, for a large portion of the time. This autonomous path also gives us greater flexibility in being able to also score on another set of flags, for example, the center flag. Again, the “prime” variation of this exists, which allows us to start pointed towards the flags (as if we were doing auton #1).
# Front Auton path #3
* start pointed towards ball
* Drive forward
* Pick up ball
* Point turn
* High flag (center post)
* Mid flag (center post
* Low flag (center post)
* Drive backwards
* Point turn
* Drive forward
* Low flag
This auton is exclusiely “collaboration”. This allows our alliance to score all of our flags, which is a very big point swing. It is very risky, as we are very close to the autonomous line the entire time - if one sensor count is wrong, there’s a big issue. This also has a prime version, which allows us to confuse the enemy even more
# Front Auton path #4
* drive forward and do nothing
Front Auton path #5
* sit and do nothing
These autons will be run if we don’t have anything to do that match, or don’t want our point swing to be too large (for whatever reason if we wanted to NOT have high ap). These are also good backups if our robot has broken.
Now, let’s talk about the rear auton paths. These also have “prime” positions, but those are selected not with the position pot, but with the path pot. This is because we don’t have enough resolution on the position pot, and instead have to use the path pot.
# Rear Auton #1
* drive forward
* Hit top flag of our post
* Hit low flag of our post
This is the simplest rear auton, and the failure rate on this is incredibly low. The only thing that our alliance partner has to do is go and not be in the way! 
# Rear Auton #2
* point towards ball
* Drive forward
* Collect ball
* Drive backwards
* Point turn
* Drive forwards
* Hit high mid low flag of our post
This is the beefed up version of the auton #1. This is slightly riskier, for the same reasons as stated above - we might not be super great at travelling with two balls intaked. 
That’s the last thing we really have before our competition on this saturday.
