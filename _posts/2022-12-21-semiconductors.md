# Thinking through semiconductors — old nodes and AI chips
A project I’m working on forced me to wade into the discourse about semiconductors – especially the economics of older chip manufacturing processes and claims about the importance of bleeding edge processes for AI. I wrote this piece mostly to clarify my own understanding but I thought it might be useful to other people. 

Some really dumb preliminaries. Skip this if you know about semiconductor manufacturing:
* Semiconductors are manufactured on silicon *wafers* — older nodes used 200mm diameter wafers and newer nodes (after ~2000) use 300mm diameter wafers.
* Each wafer can hold one or more *chips* — these are the discrete units that comprise electronics.
* Chips are made of many *devices* that the manufacturing process embeds in silicon through many steps of subtraction (etching via photolithography) and addition (chemical deposition, etc.) The primary device people talk about in computing is the transistor, but devices can also be sensors, resistors, capacitors, etc.
* The *node size* refers approximately to the smallest device feature (like the gate of a transistor) that a specific process can create. As node sizes get smaller, you can make transistors more dense, so you can have more transistors per mm^2 and thus have more transistors per wafer, and thus make single chips with more transistors. This exponential growth in transistors/chip is what Moore’s law is referring to. As of 2022, the 5nm process is the most advanced node in production. The most advanced node in the mid 1990s was 180nm, which is notable because it was the first node that was smaller than the wavelength of light used to make it.

There are several numbers at play when we’re talking about the economics of chips:
* The capital expenses (capex) of creating the production line. (The production line + building that houses it are collectively referred to as a “fab”). These are one-off costs of building the building, buying the machinery, training people to operate it, and (this one often gets left out) figuring out how to get everything working.[^1]
* The recurring costs to the manufacturer — these occur per *wafer* and include consumables like ultra-pure water, chemicals, and electricity as well as labor. (Also known as operational expenses or opex.)
* The one-off costs associated with creating a new chip — design, creating the masks, testing them, and iterating.
* The price that the manufacturer can charge to manufacture a wafer.
* The price that a chip designer can charge for a chip. (Sometimes the manufacturer and the chip designer are the same, as in the case of Intel, and sometimes they are different as in the case of “fabless” companies and say, TSMC.)

There are several numbers that change monotonically as you make nodes smaller:
* The capex paid by the manufacturer to create a new fab increases. A new 5nm fab costs ~$10B; a new 180nm fab costs ~$100M.
* The cost to the manufacturer to create a single wafer increases. 
* The number of transistors on a wafer increases. 
* The power that each individual transistor uses while operating decreases.
* The price consumers will pay per chip increases.

The trick is the *relative* rate at which each of these changes happen. The price that consumers are willing to pay per chip increases faster than both opex and capex, such that the margins (and thus profit) for manufacturing more advanced nodes is significantly larger than for larger nodes. Additionally, the rate at which the number of transistors on a wafer increases is faster than the rate at which the price increases, so the price per transistor continues to decrease with node size.

It’s easy (for me) to forget that transistors are not a commodity. While 10 chips with 1B transistors each can technically do the same calculations as one chip with 10B transistors, if the single chip is made with smaller node processes, it uses less space and power. Specific customers are willing to pay premiums for that (see the next section).

Despite the world’s focus on bleeding edge chips, the majority of semiconductor consumption is in older nodes: 90% of the semiconductor market is nodes larger than 60nm and 23% of it is nodes larger than 180nm. Arduinos still use chips made using ~300nm nodes. However, the majority of the *profit* comes from the bleeding edge chips. The profit margin on bleeding edge chips is much higher because people (especially militaries and data centers) are willing to pay a premium for power efficiency and bandwidth. Car manufacturers are now a huge consumer of chips and tend to lock in on older chips. The same goes for many appliances and IoT devices.

The continuing (as of 2022) chip shortages that started in the early 2020s are primarily in older nodes, *not* cutting edge chips. So why didn’t manufacturers respond to increased demand by increasing supply. The argument from one expert is not that it’s the cost of spinning up a fab (you could raise prices to cover that). Instead it’s a combination of the *time* to spin up a fab and the cyclic nature of the semiconductor market. It takes order years to spin up even an older node fab. Based on historical trends, manufacturers believe we’re near some kind of peak, so by the time the fab is online, demand will have died down. Even older fabs are expensive enough that they need to be running near full capacity to recoup the cost of building them, so manufacturers see building new older-node capacity in response to changeable market conditions as a bad idea. By contrast, they see a monotonically increasing demand for bleeding edge nodes, as long as the bleeding edge goalpost keeps moving — hence the massive amount of R&D and new fab dollars.

It’s also notable that almost all older node machines are still in use. While you can buy them used, they’re still quite expensive because the market is very illiquid — people don’t sell machines for older node machines often and the continued demand for older node chips means the demand for a machine lasts for decades.

So there’s this weird equilibrium point around older nodes, where demand remains high but a combination of still-expensive equipment, long lead times, and market fluctuations create a situation where it’s not economically viable to respond to changing demand.

### Why do people say that leading edge nodes are essential for AI and the military?
At face value, the statement “you need cutting edge chips to do cutting edge AI” is false. You could absolutely train and run any machine learning application out there on older chip technology. However, there is still substance to the argument that the ability to create leading edge semiconductor nodes is important for the military (and other kinds of competitiveness).

The difference between the most advanced node and something slightly older means a not-insignificant difference in battery life or inference speed. While you could technically do all the same operations on two chips with 1B transistors each, a single chip with 2B transistors will do them faster, consume less power, and enable computational tricks that wouldn’t be possible if everything weren’t happening on the same chip.  A current generation GPU can be ~20% faster and more energy efficient than an older generation one.[^2]

For a data center, whose main cost is electricity (companies choose otherwise ridiculous locations to minimize electricity cost eg. near hydroelectric dams), any reduction in power consumption can lead to massive savings. Data centers pass these costs on to consumers. Training AI (and even running inference for large models) requires a ton of data center compute, so more power-efficient chips arguably play a big role in reducing the cost of training models, which in turn can determine which products are profitable or not.

In competitive situations — especially military ones — small differences in performance between your products and a competitor’s can make a huge difference. Even if a chip’s power consumption is a small fraction of a drone’s power use, even a 5% greater range means you could hit someone when they can’t hit you, etc. For a military contractor, even slightly better than a competitor means you get the contract and they don’t.

Relative performance is one of those situations where continuous changes can lead to discrete differences. In this case, the threshold has to do with *how good your thing’s performance is compared to other things*. It’s not that there’s any application you *can’t* do with older nodes, it’s that you will do it less performantly. The military is obviously willing to pay premiums for small performance boosts. Apparently the market is such that other consumers are as well.

Autonomous cars are a funny side case. People often point to them as a demand driver for more efficient GPUs, which confused me because an electric car running a GPU at full blast will only reduce its battery life by ~1%.[^3] It turns out that the real reason that cutting edge chips are important for autonomous cars is that “automotive grade” chips need to stay within a specific temperature range. If you have engine heat and the sun beating down on a big metal box, the computation itself can only generate so much heat and still stay within an acceptable temperature range. Thus, the more efficient your chip, the more computation you can do and still stay within the allowed temperature range.  

The upshot of all of this is that when people say “bleeding edge chips are essential for AI” — what they actually mean is that bleeding edge chips give one AI system an advantage over another, or create efficiency differences that can cross some temperature or cost threshold.

### Conclusion
* Older node chips are still used heavily but are drastically less profitable.
* Manufacturers are hesitant to respond to increased demand for older chips because they expect the demand to be cyclic while spinning up trailing edge fabs is still expensive and takes a long time, so by the time you got the fabs online, they wouldn’t be running at full capacity and it would be very hard to recoup the costs. 
* Bleeding edge chips are important for AI because relative quality matters for militaries and business and because increased efficiency can cross cost and temperature thresholds.


## Acknowledgements
Thanks to Austin Vernon and Oren Hazi for reading drafts of this (and to Oren for extensive, extremely helpful comments). And thanks to Jay Goldberg for a very helpful conversation. 

[^1]: Even building a not-bleeding-edge fab requires a lot of tacit knowledge. The machines are not plug and play: you need to figure out new settings and processes for each fab. There is a lot of trial-and-error and finger knowledge in getting everything to work right. On top of that, the number of people with this knowledge (especially for older nodes) is decreasing thanks to a combination of industry consolidation, an aging workforce, and more lucrative opportunities for people with the sort of skills you need to set up a fab.
[^2]:https://www.tomshardware.com/news/amd-zen-4-ryzen-7000-has-810-ipc-uplift-more-than-35-overall-performance-gain
[^3]: A high-end battery is ~100kWh; power consumption at 60mph is ~14kW; a GPU at full capacity is ~200W. So range consuming 14.2 kW = 423 mi while range consuming 14 kW = 429 mi —> ~1% difference.

#publishing/unpublished
